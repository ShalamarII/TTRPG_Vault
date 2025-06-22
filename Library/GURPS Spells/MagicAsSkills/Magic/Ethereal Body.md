---
tags:
  - Spell
  - SpellsAsMagic
spellID: pzGMLWIGJFS8FVLa6 
spellName: Ethereal Body
spellCollege: [Movement]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 sec"'
spellCastingTime: '"30 sec"'
spellCost: "8"
spellMaintenance: "4"
spellPrerequisites: [Magery 3, Movement 3, Body Of Air, 6 Spell(s) from the Movement College, ]
spellPrereqText: Magery 3, Movement 3, Body Of Air, 6 Spell(s) from the Movement College
spellSource: Magic
spellReference: M146
spellLink: [[Magic.pdf#page=148&search=Ethereal Body]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic.pdf#page=148&search=Ethereal Body|Spell Link]]

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