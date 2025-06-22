---
tags:
  - Spell
  - SpellsAsMagic
spellID: pMquTdzlaA3kQi7pQ 
spellName: Long March
spellCollege: [Movement]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: ST
spellDuration: '"1 day"'
spellCastingTime: '"1 min"'
spellCost: "3"
spellMaintenance: "-"
spellPrerequisites: [Debility, Clumsiness, Magery 1, Movement 1, ]
spellPrereqText: Debility, Clumsiness, Magery 1, Movement 1
spellSource: Magic
spellReference: M143
spellLink: [[Magic.pdf#page=145&search=Long March]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic.pdf#page=145&search=Long March|Spell Link]]

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