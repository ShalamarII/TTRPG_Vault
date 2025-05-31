---
tags:
  - Spell
  - PowersAsMagic
impulse: Move
aspect: Air
spellCost: "4"
fpCost: "2"
castTime: "1"
duration: 
spellType: Missile
---
---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Battering Barrage </span>
```dataview 
TABLE WITHOUT ID 
spellType as "Spell Type", spellCost as "Vraul Cost", fpCost as "FP Cost", castTime as "Cast Time", duration as "Duration (Minutes)", impulse as "Impulse", aspect as "Aspect"
FROM "Library" 
WHERE file.path = this.file.path
SORT spellCost ASC
```

You launch a barrage of force missiles at a single target. Use Innate Attack (Projectile) to hit, applying normal range penalties. This attack has RoF 7 and Recoil 1. It does 1d crushing damage per level of this spell, affecting even insubstantial targets. Damage is doubled for the purpose of knockback. The missiles can be blocked.


---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;">Weapon Statistics</span>

| Damage      | 1/2 Damage Range | Max Range | Accuracy | Rate of Fire | Shots | Recoil | Resist |
| ----------- | ---------------- | --------- | -------- | ------------ | ----- | ------ | ------ |
| 1d crushing | 50               | 100       | 3        | 1            | 7     | 1      | null   |

---
<span style="display: flex; justify-content: center; font-size: 24; font-weight: bold;"> Modifier List </span>

|   |   |   |
|---|---|---|
|Modifiers|Cost|Notes|
|[BasicSpell](https://alrathion-the-ends-fall.tiddlyhost.com/#BasicSpell)|-30%|"Costs FP, Requires IQ roll, Magical/Divine/Spirit/Nature"|
|[verbal](https://alrathion-the-ends-fall.tiddlyhost.com/#verbal)|-5%|"Single/quiet word"|
|[Somatic](https://alrathion-the-ends-fall.tiddlyhost.com/#Somatic)|-10%|"Large gestures with both hands"|
|[Additional Projectile (5)](https://alrathion-the-ends-fall.tiddlyhost.com/#Additional%20Projectile%20%285%29)|+100%|"Must be taken with Rapid Fire. Adds an additional projectile. Only works with Innate Attack (Projectile))"|
|[Additional Projectile (1)](https://alrathion-the-ends-fall.tiddlyhost.com/#Additional%20Projectile%20%281%29)|+20%|"Must be taken with Rapid Fire"|
|[Increased 1/2D x5](https://alrathion-the-ends-fall.tiddlyhost.com/#Increased%201%2F2D%20x5)|+10%|"1/2D is 50% of Max"|
|[Aspect - Air](https://alrathion-the-ends-fall.tiddlyhost.com/#Aspect%20-%20Air)|+200%|"Air is a fickle thing, breezing by as quickly as time itself."|
|[Impulse - Move](https://alrathion-the-ends-fall.tiddlyhost.com/#Impulse%20-%20Move)|+0%|"1/2xBasic Lift. "|

|   |   |
|---|---|
|Innate Attack|Notes|
|[Innate Attack (Crushing)](https://alrathion-the-ends-fall.tiddlyhost.com/#Innate%20Attack%20%28Crushing%29)|"Your attack inflicts damage through blunt impact, like a bludgeoning weapon or an explosive blast. It is likely to cause knockback (p. 378), and is more effective at inflicting blunt trauma (p. 379) than other types of damage."|

---
