# packs

NorthByte's own Minecraft datapacks and resource packs, for Minecraft Java 26.2.

Each pack is one dual-use zip: install it as a datapack and it adds recipes, items and
paintings; load it as a resource pack and those items get their textures. Every pack is
published as its own project on Modrinth under the NorthByte organization.

## Packs

| Pack | Status |
| --- | --- |
| `kentucky-fried-creeper/` | Planned (2026-09-27). Fried-chicken parody: food items and a sign. |

## Layout

```
<pack>/
  pack.mcmeta     one file, covers data/ and assets/
  data/           datapack half: recipes, painting variants
  assets/         resource pack half: models, item definitions, textures
  art/            scripts that render the textures in assets/
tools/            shared build tooling
openspec/         planned changes and specs
```

## Installing

- **Singleplayer:** put the zip in `saves/<world>/datapacks/` and in `resourcepacks/`.
- **Server:** put the zip in `world/datapacks/`, and serve it as the resource pack.

## Licence

Not chosen yet. Nothing is published until it is.
