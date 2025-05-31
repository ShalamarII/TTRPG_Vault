---
tags:
  - Spell
  - PowersAsMagic
impulse: Protect
aspect: Body
spellCost: "3"
fpCost: "2"
castTime: "2"
duration: "60"
spellType: Buff
---
---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Absorb Impact </span>
```dataview 
TABLE WITHOUT ID 
spellType as "Spell Type", spellCost as "Vraul Cost", fpCost as "FP Cost", castTime as "Cast Time", duration as "Duration (Minutes)", impulse as "Impulse", aspect as "Aspect"
FROM "Library" 
WHERE file.path = this.file.path
SORT spellCost ASC
```

The subject gains DR 2 per level of this spell against fall and collision damage for the duration of the spell. The velocity of a falling subject is not altered. Reduced damage will be suffered upon landing on a normal surface (spikes, etc. would still do full damage). This DR counts as innate armor, i.e. is not considered flexible when calculating blunt trauma due to collisions and falls.


---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;">Weapon Statistics</span>

| Damage | 1/2 Damage Range | Max Range | Accuracy | Rate of Fire | Shots | Recoil | Resist       |
| ------ | ---------------- | --------- | -------- | ------------ | ----- | ------ | ------------ |
|        |                  | 100       | 3        | 1            | N/A   | 1      | (HT+1)-level |

---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Modifier List </span>

|   |   |   |
|---|---|---|
|Modifiers|Cost|Notes|
|[BasicSpell](https://alrathion-the-ends-fall.tiddlyhost.com/#BasicSpell)|-30%|"Costs FP, Requires IQ roll, Magical/Divine/Spirit/Nature"|
|[verbal](https://alrathion-the-ends-fall.tiddlyhost.com/#verbal)|-5%|"Single/quiet word"|
|[Somatic](https://alrathion-the-ends-fall.tiddlyhost.com/#Somatic)|-10%|"Large gestures with both hands"|
|[Fixed Duration](https://alrathion-the-ends-fall.tiddlyhost.com/#Fixed%20Duration)|+0%|"Afflictions default to 3 minutes"|
|[Increased 1/2D x10](https://alrathion-the-ends-fall.tiddlyhost.com/#Increased%201%2F2D%20x10)|+15%|"1/2D is 100% of Max"|
|[No Signature](https://alrathion-the-ends-fall.tiddlyhost.com/#No%20Signature)|+20%||
|[Impulse - Protect](https://alrathion-the-ends-fall.tiddlyhost.com/#Impulse%20-%20Protect)|+0%|"Barriers and ethereal borders help with the protection of one's self. The main spell type used on reaction/on Active Defense"|
|[Aspect - Body](https://alrathion-the-ends-fall.tiddlyhost.com/#Aspect%20-%20Body)|+200%|"Body, the very vessel that contains beings in the world."|

|   |   |
|---|---|
|Innate Attack|Notes|
|[Affliction (Advantage) - Innate Attack](https://alrathion-the-ends-fall.tiddlyhost.com/#Affliction%20%28Advantage%29%20-%20Innate%20Attack)|"1/2D 10, Max 100, Acc 3, RoF 1, Shots N/A, and Recoil 1 with resist (HT+1)-level"|

---
