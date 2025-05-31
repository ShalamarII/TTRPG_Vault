```dataview 
TABLE WITHOUT ID 
file.link AS "Spells", spellCost as "Vraul Cost", castTime as "Cast Time", impulse as "Impulse", aspect as "Aspect"
FROM "Library" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Spell")
SORT spellCost ASC
```

---
```dataview 
TABLE WITHOUT ID 
file.link AS "Aspect", manaCost as "Vraul Cost", characterPointCost as "Character Points Required", requiredRealm as "Required Realm"
FROM "Library" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Nouns")
SORT spellCost ASC
```
---
```dataview 
TABLE WITHOUT ID 
file.link AS "Impulse", fpCost as "FP Cost", castTime as "Cast Time"
FROM "Library" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Verbs")
SORT spellCost ASC
```
---