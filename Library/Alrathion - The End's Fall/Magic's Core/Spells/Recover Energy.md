---
tags:
  - Spell
  - PowersAsMagic
impulse: Sustain
aspect: Body
spellCost: "3"
fpCost: "2"
castTime: "1"
duration: infinite
spellType: Buff
---
---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Recover Energy </span>
```dataview 
TABLE WITHOUT ID 
spellType as "Spell Type", spellCost as "Vraul Cost", fpCost as "FP Cost", castTime as "Cast Time", duration as "Duration (Minutes)", impulse as "Impulse", aspect as "Aspect"
FROM "Library" 
WHERE file.path = this.file.path
SORT spellCost ASC
```

While this spell is active, you recover 1 FP per minute. This spell does not cost any FP and does not need to be maintained.


---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;">Weapon Statistics</span>

| Damage | 1/2 Damage Range | Max Range | Accuracy | Rate of Fire | Shots | Recoil | Resist |
| ------ | ---------------- | --------- | -------- | ------------ | ----- | ------ | ------ |
|        |                  |           |          | 1            | N/A   | 1      | null   |

---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Modifier List </span>

|   |   |   |
|---|---|---|
|Modifiers|Cost|Notes|
|[BasicSpell](https://alrathion-the-ends-fall.tiddlyhost.com/#BasicSpell)|-30%|"Costs FP, Requires IQ roll, Magical/Divine/Spirit/Nature"|
|[verbal](https://alrathion-the-ends-fall.tiddlyhost.com/#verbal)|-5%|"Single/quiet word"|
|[Somatic](https://alrathion-the-ends-fall.tiddlyhost.com/#Somatic)|-10%|"Large gestures with both hands"|
|[Aspect - Body](https://alrathion-the-ends-fall.tiddlyhost.com/#Aspect%20-%20Body)|+200%|"Body, the very vessel that contains beings in the world."|
|[Impulse - Sustain](https://alrathion-the-ends-fall.tiddlyhost.com/#Impulse%20-%20Sustain)|+0%|"Sustain, just as nature itself."|
|[Self Only](https://alrathion-the-ends-fall.tiddlyhost.com/#Self%20Only)|-20%|"Directs the spell at yourself only, instead of being in touch range."|

---
