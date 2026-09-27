# Kentucky Fried Creeper

A fried-chicken parody pack for vanilla **Minecraft Java 26.2 only**: four foods and a shop sign,
all crafted in survival from vanilla ingredients. No mods, no plugins.

One zip is both halves: the datapack adds the items and recipes, the resource pack draws them.
Without the resource pack everything still works and names still read in English, but the items
and the sign show the missing-texture pattern.

## Installing

- **Singleplayer:** put the zip in `saves/<world>/datapacks/` and in `resourcepacks/`, then
  enable it in the resource pack screen.
- **Server:** put the zip in `world/datapacks/` and **restart** the server. `/reload` is not
  enough: the sign is a new painting variant, and those load only at startup. Serve the same zip
  as the resource pack.

Removing the pack from a world deletes every placed sign.

## Recipes

| Result | Ingredients | Grid |
| --- | --- | --- |
| 1 Creeper Drumstick | 1 cooked chicken, 1 wheat, 1 gunpowder | any arrangement |
| 1 Bucket of Creeper | 3 cooked chicken, 1 gunpowder, 3 paper | crafting table, shape below |
| 2 Hot Wings | 2 cooked chicken, 1 blaze powder | any arrangement |
| 1 Kentucky Fried Creeper sign | 1 painting, 1 red dye, 1 white dye, 1 cooked chicken | any arrangement |

Bucket of Creeper (C cooked chicken, G gunpowder, P paper):

```
C G C
P C P
  P
```

Every pack item counts as its vanilla base in any recipe: the foods as cooked chicken, the Empty
Creeper Bucket as paper. No recipe gives back more than the chicken it takes. Recipes unlock in
the recipe book when you first hold cooked chicken (the foods) or a painting (the sign).

## Items

| Item | Eat time | Hunger | Saturation | Effect | Stack |
| --- | --- | --- | --- | --- | --- |
| Creeper Drumstick | 1.6 s | 8 | 9.6 | Eat while sprinting, at full speed | 64 |
| Bucket of Creeper | 3.2 s | 20 | 20 | Creeper hiss, Slowness I for 15 s, leaves an Empty Creeper Bucket | 16 |
| Hot Wings | 0.8 s | 5 | 6 | Fire Resistance for 10 s | 64 |

- **Empty Creeper Bucket:** not food. Wear it on your head: use it from the hotbar or put it in
  the helmet slot. Only obtainable by finishing a Bucket of Creeper. Stacks to 1.
- **Kentucky Fried Creeper sign:** a 4x2 painting by NorthByte. Only obtainable by crafting; an
  ordinary painting never rolls it.

Names and descriptions are in English and Swedish, following the client language.

## Give commands

For operators and testing:

```
/loot give @s loot fried_creeper:items/creeper_drumstick
/loot give @s loot fried_creeper:items/bucket_of_creeper
/loot give @s loot fried_creeper:items/empty_creeper_bucket
/loot give @s loot fried_creeper:items/hot_wings
/loot give @s loot fried_creeper:items/sign
```

## Source

Textures are drawn by the scripts in `art/`; `task render PACK=kentucky-fried-creeper` rewrites
them. `task build PACK=kentucky-fried-creeper VERSION=<v>` builds the zip.

## Licence

[CC0 1.0](../LICENSE): public domain, no attribution required.
