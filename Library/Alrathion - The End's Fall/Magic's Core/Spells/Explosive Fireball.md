---
tags:
  - Spell
  - PowersAsMagic
spellCost: "4"
impulse: Create
aspect: Fire
castTime: "1"
fpCost: "3"
duration: 
spellType: Missile
---
---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;">Explosive Fireball</span> 
```dataview 
TABLE WITHOUT ID 
spellType as "Spell Type", spellCost as "Vraul Cost", fpCost as "FP Cost", castTime as "Cast Time", duration as "Duration (Minutes)", impulse as "Impulse", aspect as "Aspect"
FROM "Library" 
WHERE file.path = this.file.path
SORT spellCost ASC
```

Creates a fireball that affects both its target and things nearby. This has 1/2D 25, Max 50, Acc 1. Can be thrown at a wall, floor, etc. (at +4 to hit) to catch foes in the blast. The target and anyone closer to the target than one yard takes full damage. Those further away divide damage by three times their distance in yards (round down).

---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;">Weapon Statistics</span>

| Damage | 1/2 Damage Range | Max Range | Accuracy | Rate of Fire | Shots | Recoil |
| ------ | ---------------- | --------- | -------- | ------------ | ----- | ------ |
| 2d     | 25               | 50        | 1        | 1            | N/A   | 1      |

---

| Modifiers                                                                                                      | Cost  | Notes                                                      |
| -------------------------------------------------------------------------------------------------------------- | ----- | ---------------------------------------------------------- |
| [BasicSpell](https://alrathion-the-ends-fall.tiddlyhost.com/#BasicSpell)                                       | -30%  | "Costs FP, Requires IQ roll, Magical/Divine/Spirit/Nature" |
| [Verbal](https://alrathion-the-ends-fall.tiddlyhost.com/#Verbal)                                               | -10%  | "Many/loud words"                                          |
| [Somatic](https://alrathion-the-ends-fall.tiddlyhost.com/#Somatic)                                             | -10%  | "Large gestures with both hands"                           |
| [Reduced Ranged 1/4](https://alrathion-the-ends-fall.tiddlyhost.com/#Reduced%20Ranged%201%2F4)                 | -15%  | "Max 25 yds"                                               |
| [Increased 1/2D x5](https://alrathion-the-ends-fall.tiddlyhost.com/#Increased%201%2F2D%20x5)                   | +10%  | "1/2D is 50% of Max"                                       |
| [Area Effect: 4 yd radius](https://alrathion-the-ends-fall.tiddlyhost.com/#Area%20Effect%3A%204%20yd%20radius) | +100% | "7 hex dia."                                               |
| [Impulse - Create](https://alrathion-the-ends-fall.tiddlyhost.com/#Impulse%20-%20Create)                       | +100% | "Creates/Manifests a magical phenomena"                    |
| [Extra 1d of Damage](https://alrathion-the-ends-fall.tiddlyhost.com/#Extra%201d%20of%20Damage)                 | +100% | "An extra d of damage"                                     |

| Innate Attack                                                                                        | Notes                                                                                                          |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [Innate Attack (Burn)](https://alrathion-the-ends-fall.tiddlyhost.com/#Innate%20Attack%20%28Burn%29) | "Your attack inflicts damage using flame, an energy beam, or localized electrical burns. It may ignite fires!" |

---