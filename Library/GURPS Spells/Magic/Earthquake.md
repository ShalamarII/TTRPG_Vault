---
tags:
  - Spell
  - SpellsAsMagic
spellID: ph6qb8mHjRXOECfy- 
spellName: Earthquake
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"30 sec"'
spellCost: "2"
spellMaintenance: "Same"
spellPrerequisites: [Magery 2, Earth 2, 5 Spell(s) from the Earth College, Earth Vision, ]
spellPrereqText: Magery 2, Earth 2, 5 Spell(s) from the Earth College, Earth Vision
spellSource: Magic
spellReference: M54
spellLink: [[Magic.pdf#page=56&search=Earthquake]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic.pdf#page=56&search=Earthquake|Spell Link]]

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