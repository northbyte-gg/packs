## Context

See proposal.md for why. The repo holds nothing but its constitution; this change adds the first
pack and the tooling every later pack reuses. Behaviour is fixed in `specs/`; this document says
how the pack produces it on 26.2.

Every format number and component name below was read on 2026-09-27 from Minecraft Java 26.2
itself (released 2026-06-16), not from memory. The sources:

| Id | Source |
| --- | --- |
| S1 | `server-26.2.jar` → `version.json`: `pack_version` resource 88.0, data 107.1 |
| S2 | Data generator `--reports` on the 26.2 server jar: `registries.json` (component, consume effect, sound, mob effect, recipe serializer registries) |
| S3 | Same run: `reports/minecraft/components/item/*.json`, the default components of every vanilla item |
| S4 | 26.2 server jar `data/minecraft/`: recipes, advancements, painting variants, the `placeable` tag, the `trade_rebalance` feature pack's `pack.mcmeta` |
| S5 | 26.2 client jar `assets/minecraft/`: `items/cooked_chicken.json`, `atlases/paintings.json` |
| S6 | `javap` on the unobfuscated 26.2 classes: `Ingredient`, `UseEffects`, `Equippable`, `UseRemainder`, `PlaySoundConsumeEffect`, `ApplyStatusEffectsConsumeEffect`, `TranslatableContents`, `PackFormat`, client `CustomHeadLayer` |

`tools/reference` (task 1.1) regenerates S1 to S3 for any version, so every citation can be
re-checked.

## Goals / Non-Goals

**Goals:**
- Every identifier is decided here, before any file exists, because each becomes permanent at the
  first release.
- The three mechanics nobody has seen working on 26.2 get tested before any art is drawn:
  sprint-eating, a paper item rendered on the head, and one `pack.mcmeta` accepted by both loaders.
- The tooling is small, repo-wide and pack-agnostic, so the second pack costs only content.

**Non-Goals:**
- Modrinth publishing (a later change).
- Installing the pack on NorthByte's servers. That happens in the private deployment repo, with its
  own staging trial.
- Custom blocks, entities, functions that run every tick, or anything the player can see only with
  a mod.
- Supporting any version other than 26.2.

## Decisions

### D1. Identifiers (permanent from v1.0.0)

Namespace `fried_creeper`. Pack directory and release name `kentucky-fried-creeper`.

| Kind | Ids |
| --- | --- |
| Item model | `fried_creeper:creeper_drumstick`, `fried_creeper:bucket_of_creeper`, `fried_creeper:empty_creeper_bucket`, `fried_creeper:hot_wings` |
| Recipe | `fried_creeper:creeper_drumstick`, `fried_creeper:bucket_of_creeper`, `fried_creeper:hot_wings`, `fried_creeper:sign` |
| Advancement (recipe unlock) | `fried_creeper:recipes/<recipe>` for each of the four recipes |
| Painting variant | `fried_creeper:sign` |
| Loot table (give aid) | `fried_creeper:items/<item model>` for the four items, plus `fried_creeper:items/sign` |
| Translation key | `item.fried_creeper.<item model>` and `item.fried_creeper.<item model>.desc` |

The loot tables exist so an operator or a tester can run
`/loot give @s loot fried_creeper:items/creeper_drumstick` instead of typing components by hand.
They are also the third copy of each item's components, which is why the lint compares copies.

### D2. Base items

A 26.2 recipe ingredient is a set of item types and nothing more: `Ingredient` holds a
`HolderSet<Item>` (S6), and no recipe in S4 matches on components. Every pack item therefore
counts as its base item in every recipe. The bases follow from that:

| Item | Base | Why |
| --- | --- | --- |
| Creeper Drumstick, Bucket of Creeper, Hot Wings | `minecraft:cooked_chicken` | Used as an input by no vanilla recipe (S4), so it leaks nowhere. Wolves already eat it. Feeding pack food back into pack recipes never gains items (spec: "Recipes cannot multiply food") |
| Empty Creeper Bucket | `minecraft:paper` | A plain item with no use action. It can stand in for paper, including in the next Bucket of Creeper: the bucket gets recycled, and no food appears from nothing |
| Sign | `minecraft:painting` | The vanilla painting item with the `painting/variant` component (S2, S3) |

Rejected: `minecraft:bucket` as the Empty Creeper Bucket's base. A bucket's own use action picks
up water, and the result would be a water bucket. Also rejected: `cooked_chicken` with
`!minecraft:food` removed. The empty bucket would then count as cooked chicken, and eat bucket,
reuse bucket as chicken, craft bucket becomes a loop that makes food.

### D3. Components

Names and fields per S2, S3 and S6. Values per `specs/kentucky-fried-creeper/spec.md`.

| Item | Components set |
| --- | --- |
| All four items | `item_model` (D1); `item_name` and `lore`, each a translatable text with `fallback` (field present in `TranslatableContents`, S6); lore `color: gray`, `italic: false` |
| Creeper Drumstick | `food` `{nutrition: 8, saturation: 9.6}`; `use_effects` `{can_sprint: true, speed_multiplier: 1.0}` (the fields spears set in S3) |
| Bucket of Creeper | `food` `{nutrition: 20, saturation: 20}`; `consumable` `{consume_seconds: 3.2, on_consume_effects: [play_sound entity.creeper.primed, apply_effects slowness 300 ticks amplifier 0]}`; `use_remainder` = the Empty Creeper Bucket stack; `max_stack_size: 16` |
| Empty Creeper Bucket | `equippable` `{slot: head, swappable: true}` with no `asset_id` and no `camera_overlay`; `max_stack_size: 1` |
| Hot Wings | `food` `{nutrition: 5, saturation: 6}`; `consumable` `{consume_seconds: 0.8, on_consume_effects: [apply_effects fire_resistance 200 ticks]}` |
| Sign (painting item) | `painting/variant: fried_creeper:sign` |

Field shapes come from vanilla items in S3: `consumable` from `honey_bottle`, `use_remainder` from
`rabbit_stew`, `equippable` from `carved_pumpkin` and `leather_helmet`. `entity.creeper.primed`,
`slowness` and `fire_resistance` are in the S2 registries. `consumable` defaults (1.6 s, eat
animation, eat sound) are what `cooked_chicken` carries in S3, so the drumstick sets none.

### D4. `item_model`, not `custom_model_data` on vanilla item definitions

Each item points `item_model` at its own definition under `assets/fried_creeper/items/`, in the
shape of S5's `items/cooked_chicken.json`. No file under `assets/minecraft/` is touched.

The alternative keeps the vanilla texture for players without the resource pack: override
`assets/minecraft/items/cooked_chicken.json` and select on `custom_model_data`. It was rejected
because servers merge several resource packs into one, and packs that override vanilla item
definitions collide file by file. Dungeons and Taverns 5.3.2, for one, overrides four. A namespaced
definition cannot collide. The cost is that a player without the resource pack sees the
missing-texture pattern, and the constitution's "playable without the resource pack" principle is
amended to say exactly that (task 1.3). Names stay readable through D3's fallbacks.

### D5. One `pack.mcmeta` for both loaders

```json
{ "pack": { "description": "Kentucky Fried Creeper: a fried-chicken parody",
            "min_format": 88, "max_format": [107, 1] } }
```

The 26.2 feature pack in S4 uses `min_format`/`max_format` with `[major, minor]`. The range has to
contain resource 88.0 and data 107.1 (S1), so it spans both. The validator in `PackFormat` (S6)
demands the legacy `pack_format` field only when a range reaches back to resource format 64 or
data format 81. The minimum here is 88, so no legacy field is needed.

Rejected: `[107, 1]` to `[107, 1]`, which is what Dungeons and Taverns ships. That is exact for
data but marks the resource side incompatible, and the spec forbids that warning.

### D6. The Empty Creeper Bucket on the head

With `equippable` set and no `asset_id`, the client should draw the item model itself on the head.
`CustomHeadLayer` carries an item scale for exactly that (S6), but nobody has seen it for this
item, so task 2.3 tests it before the model is built. The item definition selects on display
context: a flat 16x16 sprite in the inventory, a small 3D bucket model on the head and in hand.

### D7. Texture art

Textures are Python scripts under `kentucky-fried-creeper/art/`, each a palette plus a character
grid rendered with Pillow, per constitution principle V. Sizes follow vanilla: 16x16 items, 16 px
per block for the sign (64x32), 64x64 `pack.png`. Previews at 16x, nearest-neighbour, go to
`dist/preview/`.

### D8. Tooling shape

`Taskfile.yml` at the repo root, as in the workspace's other repos, calling plain Python in
`tools/`: `task reference VERSION=26.2`, `task render PACK=…`, `task lint PACK=…`,
`task build PACK=… VERSION=…`, `task release PACK=… VERSION=…`.

- **reference:** downloads the version's jars through Mojang's version manifest, checks the SHA-1
  the manifest gives, and runs the data generator in a `eclipse-temurin:25-jdk` container (26.2
  declares Java 25). Output goes to `~/.cache/northbyte-packs/<version>/`, outside every git tree:
  the jars are Mojang's and are never committed.
- **lint:** stdlib Python plus the reference cache. It checks everything the `pack-build` spec
  lists. "Previous release" means the zip attached to the newest `<pack>/v*` tag, fetched with
  `gh`; with no tag, that check is skipped and the lint says so.
- **build:** a Python `zipfile` with sorted entries, a fixed 1980-01-01 timestamp and fixed
  permissions, so the same commit gives the same SHA-256.
- **release:** `gh release create <pack>/v<version>` with the zip and its SHA-256. It never uses
  `--clobber`.

### D9. Release channel

GitHub releases on `northbyte-gg/packs`. The asset is `kentucky-fried-creeper-<version>.zip`: a
versioned name, so each immutable release maps to exactly one file. GitHub immutable releases
(currently `enabled: false`) are switched on with the owner's go-ahead before v1.0.0, so a
published asset can never be swapped under the same URL.

## Risks / Trade-offs

- [Sprint-eating is inferred, not seen: `use_effects` is what 26.2 spears set, and whether it covers
  eating is untested] → Task 2.2 tests it on a 26.2 client before any art is drawn. If it fails,
  the drumstick requirement goes back to the owner, not silently dropped.
- [A paper item may not render on the head] → Task 2.3 tests it first. Fallback: an equipment asset
  (`asset_id` plus a humanoid texture layer), the way helmets render.
- [The resource range 88 to 107.1 claims formats that do not exist yet, so a future client up to
  107 loads the pack without a warning] → The pack targets 26.2 only. A target-version bump is its
  own change and re-tests.
- [The data range also admits older game versions from format 88 up, which may reject 26.2
  components] → The README says 26.2 only. Servers pin an exact release.
- [A Bucket of Creeper counts as cooked chicken, so a player can feed one to a wolf or waste one in
  a recipe] → Accepted. No recipe gains items, and the lint enforces that.
- [An Empty Creeper Bucket counts as paper] → Accepted and even useful: it recycles into the next
  bucket.
- [Drumstick sprint-eating is an edge in PvP modes where players bring their own food] → Out of
  scope here. The proposal flags it for the deployment side.
- [A slash in the tag (`kentucky-fried-creeper/v1.0.0`) ends up in the download URL] → Task 6.3
  downloads the asset by URL and compares its SHA-256.

## Migration Plan

This is a new pack with no previous state. Release v1.0.0 only after every task in section 5
passes. A bad release is fixed by a new version; a release is never deleted or replaced, because
signs placed from it depend on its ids. Rollback on a server belongs to the deployment repo, and
removing the pack there deletes every placed sign (constitution principle IV).

## Open Questions

- Should the Empty Creeper Bucket get a see-through-bucket `camera_overlay`, like the carved
  pumpkin's? It's left out of v1 and can be added later without changing any id.
