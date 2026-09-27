## Why

NorthByte wants a fried-chicken parody pack, "Kentucky Fried Creeper", playable in vanilla
Minecraft Java 26.2 with no mods or plugins. It is the first pack in this repo, so it also has
to establish how a pack is built, checked and released.

## What Changes

- New pack `kentucky-fried-creeper/`: one dual-use zip (datapack + resource pack), namespace
  `fried_creeper`, targeting Minecraft Java 26.2 only.
- Five v1 items, each crafted from vanilla ingredients in one step:
  - **Creeper Drumstick**: food, better than cooked chicken, and the only item a player can eat
    while sprinting.
  - **Bucket of Creeper**: a full meal that ends in a creeper fuse hiss and a short slowness
    ("food coma"), and leaves an Empty Bucket behind.
  - **Empty Bucket**: not food; worn on the head. Obtained only by eating a Bucket of Creeper.
  - **Hot Wings**: a fast snack that grants short fire resistance.
  - **Kentucky Fried Creeper sign**: a 4x2 painting, obtained only by crafting. It never appears
    as a random painting.
- Item names ship as translation keys with an English fallback, so a player without the
  resource pack still reads a sensible name. English and Swedish translations ship in the pack.
- Recipe book entries unlock through advancements, the way vanilla recipes do.
- New shared tooling under `tools/`: render script-drawn textures, lint the pack, build the zip,
  and cut a GitHub release.
- Releases go to **GitHub releases first**; Modrinth publishing is deferred to a later change.
  The constitution (`openspec/config.yaml`) and `README.md` are updated to say so and to name the
  pack's namespace.

## Capabilities

### New Capabilities
- `kentucky-fried-creeper`: what the pack does in game: its five items, their food and use
  behaviour, how each is obtained, the sign painting, and the names players read.
- `pack-build`: the shared tooling that renders textures, lints a pack, builds its zip and
  releases it.

### Modified Capabilities
<!-- none: this is the repo's first change and there are no existing specs -->

## Impact

- **Released identifiers:** none exist yet. This change introduces the first ones (every
  `fried_creeper:` id: item models, recipes, advancements, the painting variant). They become
  permanent at the first release, so they are fixed in design.md before any file is written.
- **New files:** `kentucky-fried-creeper/` (pack source), `tools/` (build tooling).
- **Edited files:** `openspec/config.yaml` and `README.md` (release channel, namespace).
- **Repo setting:** GitHub immutable releases, currently off on `northbyte-gg/packs`, is turned on
  before the first release, with the owner's go-ahead.
- **Downstream, out of scope here:** the servers install the release asset by URL from a separate
  private repo. That repo has its own change and its own staging trial. Two facts from this
  change feed it: the asset's filename scheme, and that the drumstick's sprint-eating is an edge
  in any PvP mode where players bring their own food.
- **Dependencies:** Python 3 with Pillow for texture rendering, `gh` for releases. The built zip
  needs neither.
