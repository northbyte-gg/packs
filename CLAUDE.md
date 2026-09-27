# packs - repo guide

🛑 **PUBLIC repo** (`northbyte-gg/packs`). Every file, commit, tag and issue is public, and so
is every published zip. No hostnames, cluster or LB addresses, namespaces, credentials or
player identities, ever. A leak removed from `HEAD` is still in pushed history.

## What this is

NorthByte's own datapacks and resource packs, one dual-use zip per pack, published to Modrinth.
Target: Minecraft Java 26.2. Deployment (the Modrinth version pin) lives in the private
`../deployments/` repo, never here.

Read `openspec/config.yaml` on entry: it is the constitution.

## Rules

- **Work flows through OpenSpec changes** (`openspec/changes/`, via `.claude/skills/openspec-*`).
  The threshold is in `openspec/config.yaml` "When to Use OpenSpec".
- **Never guess a `pack_format` or component name.** Read it from the 26.2 jar or the official
  changelog and cite it.
- **A released namespaced id is permanent.** Renaming a painting variant deletes every placed
  copy.
- **One source per texture:** a script in `<pack>/art/` or a hand-edited PNG, never both.
- **Parody only.** No real brand name, logo, mascot likeness or slogan.
- **Player text keeps å/ä/ö and has no em dashes.**
- **Never a bare `@name`** in a commit, PR, issue or release note.
- **Commit attribution:** `Co-Authored-By: Claude <noreply@anthropic.com>` or nothing.
- **Conventional Commits**, scoped by pack or `(tools)`. Tags: `<pack>/v<semver>`.
- The `openspec-*` skills are `openspec` 1.12.0 output. `openspec init` / `openspec update`
  overwrite them.
