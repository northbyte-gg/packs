## Purpose

Kentucky Fried Creeper is a fried-chicken parody pack for vanilla Minecraft Java 26.2: food items,
a wearable bucket and a shop sign, all obtained in survival by crafting from vanilla ingredients.

## ADDED Requirements

### Requirement: One zip loads as both packs on 26.2
The pack SHALL be a single zip that Minecraft Java 26.2 accepts both as a datapack and as a
resource pack, without an "incompatible" warning on either side.

#### Scenario: Installed as a datapack
- **WHEN** the zip is placed in a 26.2 world's `datapacks/` folder and the world loads
- **THEN** `/datapack list enabled` lists it and its recipes are craftable

#### Scenario: Loaded as a resource pack
- **WHEN** the same zip is selected as a resource pack on a 26.2 client
- **THEN** the client lists it as compatible and the pack's items show their own textures

### Requirement: Creeper Drumstick
A player SHALL be able to craft a Creeper Drumstick from one cooked chicken, one wheat and one
gunpowder in any arrangement, getting one drumstick. Eating it SHALL take 1.6 seconds and restore
8 hunger points and 9.6 saturation. It SHALL be the only item in the pack that a player can eat
while sprinting, at full movement speed. Drumsticks SHALL stack to 64.

#### Scenario: Crafting a drumstick
- **WHEN** a player puts one cooked chicken, one wheat and one gunpowder into a crafting grid
- **THEN** the result slot offers one Creeper Drumstick

#### Scenario: Eating while sprinting
- **WHEN** a sprinting player starts eating a Creeper Drumstick
- **THEN** the player keeps sprinting at full speed until the drumstick is eaten

#### Scenario: Other pack food slows the player
- **WHEN** a sprinting player starts eating a Bucket of Creeper or Hot Wings
- **THEN** the player stops sprinting and slows down, as with vanilla food

### Requirement: Bucket of Creeper
A player SHALL be able to craft a Bucket of Creeper in a crafting table from three cooked chicken,
one gunpowder and three paper, in this shape (C cooked chicken, G gunpowder, P paper):

```
C G C
P C P
  P
```

Eating it SHALL take 3.2 seconds and restore 20 hunger points and 20 saturation. When eaten, it
SHALL play the creeper fuse hiss, give Slowness I for 15 seconds, and leave one Empty Creeper
Bucket in the player's inventory. Nothing SHALL explode. Buckets SHALL stack to 16.

#### Scenario: Crafting a bucket
- **WHEN** a player arranges the ingredients in the shape above in a crafting table
- **THEN** the result slot offers one Bucket of Creeper

#### Scenario: Finishing a bucket
- **WHEN** a player finishes eating a Bucket of Creeper
- **THEN** the player hears the creeper fuse hiss, receives Slowness I for 15 seconds and gets one
  Empty Creeper Bucket, and no block or entity takes damage

### Requirement: Empty Creeper Bucket
The Empty Creeper Bucket SHALL be obtainable in survival only by eating a Bucket of Creeper. It
SHALL NOT be edible. A player SHALL be able to wear it on the head, either by using it from the
hotbar or by placing it in the helmet slot. It SHALL stack to 1.

#### Scenario: Putting the bucket on
- **WHEN** a player uses an Empty Creeper Bucket from the hotbar with an empty helmet slot
- **THEN** the bucket moves to the helmet slot and is visible on the player's head to other players

#### Scenario: Not edible
- **WHEN** a hungry player uses an Empty Creeper Bucket while wearing a helmet
- **THEN** no eating starts; the bucket swaps with the worn helmet

### Requirement: Hot Wings
A player SHALL be able to craft two Hot Wings from two cooked chicken and one blaze powder in any
arrangement. Eating one SHALL take 0.8 seconds, restore 5 hunger points and 6 saturation, and give
Fire Resistance for 10 seconds. Hot Wings SHALL stack to 64.

#### Scenario: Crafting wings
- **WHEN** a player puts two cooked chicken and one blaze powder into a crafting grid
- **THEN** the result slot offers two Hot Wings

#### Scenario: Eating wings
- **WHEN** a player finishes eating Hot Wings
- **THEN** the player has Fire Resistance for 10 seconds

### Requirement: Kentucky Fried Creeper sign
The pack SHALL add a painting, 4 blocks wide and 2 blocks tall, titled "Kentucky Fried Creeper"
with author "NorthByte". A player SHALL be able to craft it from one painting, one red dye, one
white dye and one cooked chicken in any arrangement. It SHALL NOT be obtainable any other way in
survival: hanging an ordinary painting SHALL never produce it.

#### Scenario: Crafting and hanging the sign
- **WHEN** a player crafts the sign and places it on a wall with a 4x2 free area
- **THEN** the Kentucky Fried Creeper sign hangs there

#### Scenario: Ordinary paintings never roll the sign
- **WHEN** a player hangs a plain painting from vanilla crafting on a 4x2 wall
- **THEN** the painting is a vanilla variant, never the Kentucky Fried Creeper sign

### Requirement: Recipes cannot multiply food
Every pack item counts as its vanilla base item in every recipe, vanilla and the pack's own, so a
Creeper Drumstick is accepted wherever cooked chicken is. No recipe in the pack SHALL output more
items than the cooked chicken it consumes, so no chain of pack recipes turns a fixed amount of
chicken into more food.

#### Scenario: Pack items fed back into pack recipes
- **WHEN** a player uses Creeper Drumsticks or Hot Wings as the cooked chicken in any pack recipe
- **THEN** the recipe works, and the player ends with no more items than the chicken put in

### Requirement: Recipe book
Each of the four crafting recipes SHALL appear in the recipe book once the player has held one of
its ingredients: cooked chicken for the drumstick, bucket and wings, a painting for the sign. A
recipe SHALL be craftable before it is unlocked, as vanilla recipes are.

#### Scenario: Unlock on first cooked chicken
- **WHEN** a player picks up cooked chicken for the first time
- **THEN** the Creeper Drumstick, Bucket of Creeper and Hot Wings recipes appear in the recipe book

### Requirement: Item names and text
Every pack item SHALL show a name and a one-line description. With the resource pack loaded,
players SHALL read them in English or Swedish, following their client language (Swedish for
`sv_se`, English otherwise). Without the resource pack, players SHALL read the English text.
Player-facing text SHALL contain no em dashes, and Swedish text SHALL keep its diacritics.

| Item | English | Swedish | Description (English / Swedish) |
| --- | --- | --- | --- |
| Creeper Drumstick | Creeper Drumstick | Creeperklubba | Secret recipe. Mostly gunpowder. / Hemligt recept. Mest krut. |
| Bucket of Creeper | Bucket of Creeper | Creeperhink | Warning: food coma. / Varning: matkoma. |
| Empty Creeper Bucket | Empty Creeper Bucket | Tom creeperhink | Wear it with pride. / Bär den med stolthet. |
| Hot Wings | Hot Wings | Heta vingar | Mouth already on fire. / Munnen brinner redan. |

#### Scenario: Swedish client
- **WHEN** a player with client language `sv_se` and the resource pack loaded hovers a Creeper
  Drumstick
- **THEN** the tooltip reads "Creeperklubba" with "Hemligt recept. Mest krut."

#### Scenario: No resource pack
- **WHEN** a player without the resource pack hovers a Creeper Drumstick
- **THEN** the tooltip reads "Creeper Drumstick" with "Secret recipe. Mostly gunpowder."

### Requirement: Playable without the resource pack
Every item, recipe and effect SHALL work for a player who has not loaded the resource pack. Only
the look changes: pack items and the sign show Minecraft's missing-texture pattern.

#### Scenario: Eating without the resource pack
- **WHEN** a player without the resource pack eats a Bucket of Creeper
- **THEN** the food, sound, effect and Empty Creeper Bucket are exactly as with the pack loaded
