---
tags:
  - Spell
  - PowersAsMagic
impulse: Heal/Harm
aspect: Body
spellCost: "6"
fpCost: "2"
castTime: "1"
duration: 
spellType: Regular
---
---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Euthanize </span>
```dataview 
TABLE WITHOUT ID 
spellType as "Spell Type", spellCost as "Vraul Cost", fpCost as "FP Cost", castTime as "Cast Time", duration as "Duration (Minutes)", impulse as "Impulse", aspect as "Aspect"
FROM "Library" 
WHERE file.path = this.file.path
SORT spellCost ASC
```

The caster painlessly kills a living willing subject. Cannot be parried or blocked, and the subject must be in C range.


---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;">Weapon Statistics</span>

| Damage | 1/2 Damage Range | Max Range | Accuracy | Rate of Fire | Shots | Recoil | Resist |
| ------ | ---------------- | --------- | -------- | ------------ | ----- | ------ | ------ |
| null   | C                | C         | null     | 1            | N/A   | 1      | null   |

---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Modifier List </span>

|   |   |   |
|---|---|---|
|Modifiers|Cost|Notes|
|[BasicSpell](https://alrathion-the-ends-fall.tiddlyhost.com/#BasicSpell)|-30%|"Costs FP, Requires IQ roll, Magical/Divine/Spirit/Nature"|
|[verbal](https://alrathion-the-ends-fall.tiddlyhost.com/#verbal)|-5%|"Single/quiet word"|
|[Somatic](https://alrathion-the-ends-fall.tiddlyhost.com/#Somatic)|-10%|"Large gestures with both hands"|
|[Heart Attack](https://alrathion-the-ends-fall.tiddlyhost.com/#Heart%20Attack)|+300%|"Gives the subject a heart attack. Can be resisted using HT-5."|
|[Impulse - Heal/Harm](https://alrathion-the-ends-fall.tiddlyhost.com/#Impulse%20-%20Heal%2FHarm)|+0%|"To heal or to harm is a gift, one that can be used for Good and Evil."|
|[Aspect - Body](https://alrathion-the-ends-fall.tiddlyhost.com/#Aspect%20-%20Body)|+200%|"Body, the very vessel that contains beings in the world."|

---
