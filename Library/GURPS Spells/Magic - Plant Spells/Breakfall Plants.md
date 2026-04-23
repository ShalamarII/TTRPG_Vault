---
tags:
  - Spell
  - SpellsAsMagic
spellID: pO0ikCoE-awAB4ffV 
spellName: Breakfall Plants
spellCollege: [Movement, Plant]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1 per 50 lbs"
spellMaintenance: "Half"
spellPrerequisites: [Magery 1, Movement 1, Plant 1, Walk Through Plants, Apportation, ]
spellPrereqText: Magery 1, Movement 1, Plant 1, Walk Through Plants, Apportation
spellSource: Magic - Plant Spells
spellReference: MPS13
spellLink: [[Magic - Plant Spells.pdf#page=13&search=Breakfall Plants]]
spellPoints: 1
spellTags: Movement, Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=13&search=Breakfall Plants|Spell Link]]

---

~~~datacorejsx
return function View(){
    return <dc.Markdown content={`~~~statblock
layout: GCS - Layout 
name: [[${dc.currentFile().field("spellLink").raw}|${dc.currentFile().field("spellName").raw}]]
spell_class: ${dc.currentFile().field("spellClass").raw}
resistedW: ${dc.currentFile().field("spellResisted").raw}
difficulty: ${dc.currentFile().field("spellDifficulty").raw}
duration: ${dc.currentFile().field("spellDuration").raw}
casting_cost: ${dc.currentFile().field("spellCost").raw}
maintenance_cost: ${dc.currentFile().field("spellMaintenance").raw}
casting_time: '${dc.currentFile().field("spellCastingTime").raw}'
college: ${dc.currentFile().field("spellCollege").raw}
prerequisites: ${dc.currentFile().field("spellPrereqText").raw}
reference: ${dc.currentFile().field("spellReference").raw}
spellLink: ${dc.currentFile().field("spellLink").raw}
spellTags: ${dc.currentFile().field("spellTags").raw}
source: ${dc.currentFile().field("spellSource").raw}
~~~`}/>
}
~~~