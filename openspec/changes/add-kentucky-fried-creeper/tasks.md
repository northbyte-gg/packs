## 1. Groundwork

- [x] 1.1 Add `tools/reference` and `task reference VERSION=<v>` (design D8): fetch the version's jars through Mojang's manifest, check their SHA-1s, run the data generator in `eclipse-temurin:25-jdk`, cache in `~/.cache/northbyte-packs/<v>/`. Verify: `task reference VERSION=26.2` leaves `version.json` showing resource 88 and data 107.1, plus `reports/registries.json`; a second run reuses the cache.
- [x] 1.2 Add `Taskfile.yml` with the five task names from D8, each stubbed to fail with "not implemented" until its group lands, and add `dist/` to `.gitignore`. Verify: `task --list` shows all five.
- [x] 1.3 Update `openspec/config.yaml`, `README.md` and `CLAUDE.md`: releases go to GitHub first and Modrinth later; the first pack's namespace is `fried_creeper`; principle II says a player without the resource pack keeps names but sees missing textures; principle IV says published GitHub releases are immutable. Verify: `openspec list --json` still parses, and `grep -n Modrinth` finds only "later" wording.

## 2. Spike: the three unseen mechanics, before any art

- [x] 2.1 Build a throwaway spike zip (scratchpad, not committed) with D5's `pack.mcmeta`, a Creeper Drumstick and an Empty Creeper Bucket (D3 components, placeholder textures), and boot a local vanilla 26.2 server in a container with it in `world/datapacks/`. Verify: the server log shows no pack or parse errors, and `/datapack list enabled` lists it.
- [x] 2.2 Owner, on a 26.2 client connected to the spike server: sprint and eat the spike drumstick. Verify: sprinting continues at full speed until it is eaten. If not, stop and take the drumstick requirement back to the owner.
  - Seen 2026-09-27 (owner, 26.2 client, spike server): sprinting continued at full speed until the drumstick was eaten.
- [x] 2.3 Owner, same session: put the spike Empty Creeper Bucket on from the hotbar and look in third person. Verify: the item model shows on the head. If not, switch D6 to an equipment asset and record it in design.md.
  - Seen 2026-09-27 (owner): the placeholder item model showed on the head in third person. D6 stands, no equipment asset.
- [x] 2.4 Owner: select the spike zip as a resource pack on the 26.2 client. Verify: the pack list shows it as compatible, with no red warning.
  - Seen 2026-09-27 (owner): the spike zip listed as compatible in the resource pack screen, no red warning; placeholder textures showed.

## 3. Tooling

- [x] 3.1 `tools/render` and `task render PACK=<p>`: run every `<p>/art/*.py`, write its PNG into `assets/`, write 16x nearest-neighbour previews to `dist/preview/`. Verify: rendering twice leaves `git status` clean, and previews exist outside the pack.
- [x] 3.2 `tools/lint` and `task lint PACK=<p>`: every check in `specs/pack-build/spec.md`. Verify: a fixtures directory holds one broken mini pack per check, each failing with its named problem, and a clean fixture passes with a single summary line.
- [x] 3.3 `tools/build` and `task build PACK=<p> VERSION=<v>`: the reproducible zip from D8, refusing when the lint fails. Verify: two builds of one commit have the same SHA-256, and `unzip -l` lists only `pack.mcmeta`, `pack.png`, `data/` and `assets/`.
- [x] 3.4 `tools/release` and `task release PACK=<p> VERSION=<v>`, with `DRY_RUN=true` printing the `gh` command instead of running it. Verify with dry runs: it refuses on a dirty tree, on an existing tag and on a failing lint, and a clean run prints the tag, asset name and SHA-256.

## 4. Pack content

- [x] 4.1 Data: four recipes, four recipe-unlock advancements, the `fried_creeper:sign` painting variant (not tagged `placeable`), and five give loot tables, all per D1 and D3. Verify: `task lint` passes, and each recipe's ingredients and counts match the spec.
- [ ] 4.2 Assets: four item definitions (the empty bucket selects on display context, D6), their models, and `en_us.json` plus `sv_se.json` in `assets/fried_creeper/lang/`. Verify: `task lint` passes its translation checks, and every string matches the spec's names table exactly.
- [ ] 4.3 Art scripts: drumstick, Bucket of Creeper, Empty Creeper Bucket (sprite plus 3D model texture), Hot Wings, the 64x32 sign, and a 64x64 `pack.png`. Verify: the owner reviews the previews in `dist/preview/` and approves each one.
- [ ] 4.4 Pack README: install steps, "26.2 only", the recipes. Verify: every recipe and value in it matches the spec.

## 5. Verification before release

- [ ] 5.1 `task lint PACK=kentucky-fried-creeper`, then `task build … VERSION=1.0.0` twice. Verify: lint clean, and identical SHA-256s.
- [ ] 5.2 Headless: boot the local 26.2 server with the built zip, `/loot spawn` each of the five give tables, and read each item entity's components. Verify: the log has no pack errors, and each item's components equal D3.
- [ ] 5.3 Owner, on a 26.2 client, walks every scenario in `specs/kentucky-fried-creeper/spec.md` against the built zip: all four recipes, eating each food, wearing the bucket, hanging the sign, at least five ordinary 4x2 paintings, recipe-book unlock, a `sv_se` client, and a client without the resource pack. Verify: each scenario is marked seen or failed, with what was seen written under this task.

## 6. Release

- [ ] 6.1 Ask the owner to enable GitHub immutable releases on `northbyte-gg/packs`; enable only after a yes. Verify: `gh api repos/northbyte-gg/packs/immutable-releases` reports `"enabled": true`.
- [ ] 6.2 `task release PACK=kentucky-fried-creeper VERSION=1.0.0`. Verify: tag `kentucky-fried-creeper/v1.0.0` exists, and its release carries `kentucky-fried-creeper-1.0.0.zip` and the SHA-256.
- [ ] 6.3 Download the asset anonymously by its public URL. Verify: its SHA-256 equals the release notes'.
- [ ] 6.4 Give the owner, for the deployment repo's own change: the asset URL, the SHA-256, the versioned filename scheme, and the note that drumstick sprint-eating matters in PvP modes where players bring their own food. Verify: delivered in the session. No file outside this repo is edited.
- [ ] 6.5 Final in-game check on a local 26.2 client with the downloaded release zip (not the local build) as datapack and resource pack: craft and eat one Creeper Drumstick, and hang the sign. Verify: write what was seen under this task.
