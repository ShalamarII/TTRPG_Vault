---
tags:
  - Spell
  - SpellsAsMagic
spellID: pqJcv-B3InFRGFOJn 
spellName: Great Haste
spellCollege: [Movement]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 sec"'
spellCastingTime: '"3 sec"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Haste, at least 12 IQ, Magery 1, Movement 1, ]
spellPrereqText: Haste, at least 12 IQ, Magery 1, Movement 1
spellSource: Magic
spellReference: M146
spellLink: [[Magic.pdf#page=148&search=Great Haste]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic.pdf#page=148&search=Great Haste|Spell Link]]

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