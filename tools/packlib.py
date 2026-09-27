"""Shared by tools/lint, tools/build and tools/release."""

import json
import os
import subprocess
import tempfile
from pathlib import Path

# The pinned target (constitution principle III). A bump is its own OpenSpec change.
TARGET = "26.2"

CACHE = Path(os.environ.get("NORTHBYTE_PACKS_CACHE", Path.home() / ".cache/northbyte-packs"))

# What the zip carries; everything else in a pack directory is source.
ZIP_ROOTS = ("pack.mcmeta", "pack.png", "data", "assets")

REPO = "northbyte-gg/packs"


class Reference:
    """Reference data for one version, produced by tools/reference."""

    def __init__(self, version=TARGET):
        self.version = version
        self.root = CACHE / version
        reg_path = self.root / "reports/registries.json"
        if not reg_path.exists():
            raise SystemExit(f"no reference data for {version}: run `task reference VERSION={version}`")
        regs = json.loads(reg_path.read_text())
        self.registries = {k: set(v["entries"]) for k, v in regs.items()}
        pv = json.loads((self.root / "version.json").read_text())["pack_version"]
        self.resource_format = (pv["resource_major"], pv["resource_minor"])
        self.data_format = (pv["data_major"], pv["data_minor"])
        self.paintings = {f"minecraft:{p.stem}" for p in (self.root / "data/minecraft/painting_variant").glob("*.json")}
        self.item_tags = {
            "minecraft:" + str(p.relative_to(self.root / "data/minecraft/tags/item").with_suffix(""))
            for p in (self.root / "data/minecraft/tags/item").rglob("*.json")
        }

    def has(self, registry, ident):
        return ns(ident) in self.registries.get(f"minecraft:{registry}", ())


def ns(ident):
    """Default the namespace to minecraft, as the game does."""
    return ident if ":" in ident else f"minecraft:{ident}"


def pack_ids(root):
    """Namespaced ids a pack defines, keyed by kind. root holds data/ and assets/ (a pack dir or
    an extracted zip). These are the ids principle IV makes permanent."""
    root = Path(root)
    ids = {}

    def collect(kind, base, sub):
        for d in sorted(root.glob(f"{base}/*/{sub}")):
            namespace = d.parent.name
            for f in sorted(d.rglob("*.json")):
                ids.setdefault(kind, set()).add(f"{namespace}:{f.relative_to(d).with_suffix('').as_posix()}")

    collect("recipe", "data", "recipe")
    collect("advancement", "data", "advancement")
    collect("painting variant", "data", "painting_variant")
    collect("loot table", "data", "loot_table")
    collect("item model", "assets", "items")
    return ids


def previous_release_zip(pack):
    """Download the zip attached to the newest <pack>/v* release. Returns (tag, path) or None."""
    out = subprocess.run(
        ["gh", "release", "list", "--repo", REPO, "--limit", "100", "--json", "tagName,createdAt"],
        check=True, capture_output=True, text=True,
    ).stdout
    tags = [r for r in json.loads(out) if r["tagName"].startswith(f"{pack}/v")]
    if not tags:
        return None
    tag = max(tags, key=lambda r: r["createdAt"])["tagName"]
    d = Path(tempfile.mkdtemp(prefix="packs-prev-"))
    subprocess.run(["gh", "release", "download", tag, "--repo", REPO, "--pattern", "*.zip", "--dir", str(d)],
                   check=True, capture_output=True)
    zips = list(d.glob("*.zip"))
    if len(zips) != 1:
        raise SystemExit(f"release {tag} has {len(zips)} zip assets, expected 1")
    return tag, zips[0]


def zip_entries(pack):
    """(arcname, path) for everything the zip carries, sorted."""
    pack = Path(pack)
    out = []
    for name in ZIP_ROOTS:
        p = pack / name
        if p.is_file():
            out.append((name, p))
        elif p.is_dir():
            out += [(f.relative_to(pack).as_posix(), f) for f in p.rglob("*") if f.is_file()]
    return sorted(out)


def write_zip(pack, dest):
    """Reproducible zip: sorted entries, fixed 1980-01-01 timestamp, fixed permissions."""
    import zipfile
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for arcname, path in zip_entries(pack):
            info = zipfile.ZipInfo(arcname, date_time=(1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            zf.writestr(info, path.read_bytes(), compresslevel=9)
