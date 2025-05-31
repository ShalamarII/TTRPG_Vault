---
tags:
  - PowersAsMagic
  - Spell
spellCost: "6"
impulse: Transform
aspect: Body
castTime: "2"
fpCost: "4"
duration: "60"
spellType: Missile
---
---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Polymorph </span>
```dataview 
TABLE WITHOUT ID 
spellType as "Spell Type", spellCost as "Vraul Cost", fpCost as "FP Cost", castTime as "Cast Time", duration as "Duration (Minutes)", impulse as "Impulse", aspect as "Aspect"
FROM "Library" 
WHERE file.path = this.file.path
SORT spellCost ASC
```

This spell transforms a creature that you can see within range into a new form.

The transformation lasts for the duration, or until the target drops to 0 hit points or dies. The new form can be any beast whose challenge rating is equal to or less than the target's (or the target's level, if it doesn't have a challenge rating).

The target's game statistics, including mental ability scores, are replaced by the statistics of the chosen beast. It retains its alignment and personality. The target assumes the hit points of its new form. When it reverts to its normal form, the creature returns to the number of hit points it had before it transformed.

If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form. As long as the excess damage doesn't reduce the creature's normal form to 0 hit points, it isn't knocked unconscious.

The creature is limited in the actions it can perform by the nature of its new form, and it can't speak, cast spells, or take any other action that requires hands or speech. The target's gear melds into the new form. The creature can't activate, use, wield, or otherwise benefit from any of its equipment.


---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;">Weapon Statistics</span>

| Damage | 1/2 Damage Range | Max Range | Accuracy | Rate of Fire | Shots | Recoil | Resist       |
| ------ | ---------------- | --------- | -------- | ------------ | ----- | ------ | ------------ |
| null   | null             | 100       | 3        | 1            | N/A   | 1      | (HT+1)-level |

---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Modifier List </span>

|   |   |   |
|---|---|---|
|Modifiers|Cost|Notes|
|[BasicSpell](https://alrathion-the-ends-fall.tiddlyhost.com/#BasicSpell)|-30%|"Costs FP, Requires IQ roll, Magical/Divine/Spirit/Nature"|
|[verbal](https://alrathion-the-ends-fall.tiddlyhost.com/#verbal)|-5%|"Single/quiet word"|
|[Somatic](https://alrathion-the-ends-fall.tiddlyhost.com/#Somatic)|-10%|"Large gestures with both hands"|
|[Reduced Ranged 1/5](https://alrathion-the-ends-fall.tiddlyhost.com/#Reduced%20Ranged%201%2F5)|-20%|"Max 20 yds"|
|[20x Duration](https://alrathion-the-ends-fall.tiddlyhost.com/#20x%20Duration)|+200%|"Makes the effects duration last longer (20x)"|
|[Aspect - Animal](https://alrathion-the-ends-fall.tiddlyhost.com/#Aspect%20-%20Animal)|+100%|"The essence of sentient life, animals are the step between creatures and humanoids."|
|[Impulse - Transform](https://alrathion-the-ends-fall.tiddlyhost.com/#Impulse%20-%20Transform)|+0%|"Many cultures have tried, and failed to do this."|

|   |   |
|---|---|
|Innate Attack|Notes|
|[Affliction (Disadvantage) - Innate Attack](https://alrathion-the-ends-fall.tiddlyhost.com/#Affliction%20%28Disadvantage%29%20-%20Innate%20Attack)|"1/2D 10, Max 100, Acc 3, RoF 1, Shots N/A, and Recoil 1 with resist (HT+1)-level"|

---
