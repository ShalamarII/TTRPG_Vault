```dataview 
TABLE WITHOUT ID 
file.link AS "Spells", spellCost as "Vraul Cost", castTime as "Cast Time", impulse as "Impulse", aspect as "Aspect"
FROM "TTRPG Systems" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Spell")
SORT spellCost ASC
```

---
```dataview 
TABLE WITHOUT ID 
file.link AS "Aspect", manaCost as "Vraul Cost", characterPointCost as "Character Points Required", requiredRealm as "Required Realm"
FROM "TTRPG Systems" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Nouns")
SORT requiredRealm ASC
```
---
```dataview 
TABLE WITHOUT ID 
file.link AS "Impulse", fpCost as "FP Cost / Realm Level", castTime as "Cast Time"
FROM "TTRPG Systems" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Verbs")
SORT spellCost ASC
```
---
```dataview 
TABLE WITHOUT ID 
file.link AS "Realms", characterPointCost as "Character Point Cost", numOfLevels as "Domain Levels"
FROM "TTRPG Systems" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Realms")
SORT spellCost ASC
```

---
```dataview 
TABLE WITHOUT ID 
file.link AS "Domains", domainNumber as "Domain Number", description as "Description"
FROM "TTRPG Systems" 
WHERE contains(tags, "PowersAsMagic") and contains(tags, "Domains")
SORT domainNumber ASC
```
---
### Mana Recovery

##### Passive Recovery
| Mana Concentration | 1hr/Amount Recovered |
| ------------------ | -------------------- |
| None               | 1                    |
| Low                | 2                    |
| Medium             | 3                    |
| High               | 4                    |


##### Active Recovery
| Mana Concentration | 1hr/Amount Recovered |
| ------------------ | -------------------- |
| None               | 2                    |
| Low                | 4                    |
| Medium             | 6                    |
| High               | 8                    |
