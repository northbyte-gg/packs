## Purpose

The shared tooling every pack in this repo goes through: rendering script-drawn textures, checking
a pack before it ships, building its zip, and releasing it on GitHub.

## ADDED Requirements

### Requirement: Textures render from scripts, deterministically
The tooling SHALL render every texture script under `<pack>/art/` into its PNG in the pack. The
same script SHALL always produce a byte-identical PNG. For review, the tooling SHALL also write an
enlarged, unsmoothed preview of each texture outside the pack.

#### Scenario: Re-rendering changes nothing
- **WHEN** the textures are rendered twice with no script changed
- **THEN** the second run leaves every committed PNG byte-identical

#### Scenario: Preview for review
- **WHEN** a texture is rendered
- **THEN** a preview at least 8 times larger, with hard pixel edges, is written outside the pack
  and is not included in any zip

### Requirement: Lint blocks a broken pack
The tooling SHALL check a pack and fail, naming each problem, when any of these hold:
- a JSON file does not parse;
- `pack.mcmeta` declares formats other than the pinned target's;
- the pack references an item, component, sound, effect or painting id that the target version
  does not have, checked against reference data generated from that version's own jar;
- a recipe outputs more items than the inputs it consumes that share the output's base item;
- two definitions of the same pack item carry different components (in a recipe result, a use
  remainder or a give table);
- a translation key used by the pack lacks an English or a Swedish entry, or a translatable name
  has no fallback text;
- player-facing text contains an em dash;
- the pack adds a painting to the random-painting pool;
- a texture that has a script differs from what the script renders;
- an identifier present in the pack's previous release is missing.

#### Scenario: Clean pack
- **WHEN** the lint runs on a pack with none of the problems above
- **THEN** it exits successfully and prints nothing but a summary line

#### Scenario: Hand-edited texture that still has a script
- **WHEN** a PNG was edited by hand but its script was not deleted
- **THEN** the lint fails and names the PNG and its script

#### Scenario: Removed released identifier
- **WHEN** a recipe, painting variant, item model or advancement id from the previous release is
  missing from the pack
- **THEN** the lint fails and names the missing id

### Requirement: Reproducible zip
The tooling SHALL build a pack into `dist/<pack>-<version>.zip` containing only what the game
reads: `pack.mcmeta`, `pack.png`, `data/` and `assets/`. Building the same commit twice SHALL
produce byte-identical zips. The build SHALL refuse to run when the lint fails.

#### Scenario: Same commit, same bytes
- **WHEN** the zip is built twice from the same commit
- **THEN** both zips have the same SHA-256

#### Scenario: Sources stay out
- **WHEN** the zip is built
- **THEN** it contains no texture scripts, previews or repo files

### Requirement: GitHub release
The tooling SHALL release a pack version by tagging `<pack>/v<version>` and creating a GitHub
release on `northbyte-gg/packs` with the zip attached and its SHA-256 in the release notes. It
SHALL refuse when the working tree is dirty, the tag already exists, or the lint fails. It SHALL
NOT publish anywhere other than GitHub.

#### Scenario: First release
- **WHEN** a clean, lint-passing pack is released as version 1.0.0
- **THEN** tag `<pack>/v1.0.0` exists and its release carries `<pack>-1.0.0.zip` and that zip's
  SHA-256

#### Scenario: Tag already exists
- **WHEN** a release is attempted for a version whose tag exists
- **THEN** the tooling stops before creating anything
