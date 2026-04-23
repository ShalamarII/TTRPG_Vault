---
tags:
  - Spell
  - SpellsAsMagic
spellID: piy55epfl1EG-16jn 
spellName: Light Tread
spellCollege: [Movement]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 min"'
spellCastingTime: '"1 sec"'
spellCost: "4"
spellMaintenance: "1"
spellPrerequisites: [Apportation, Shape Earth, ]
spellPrereqText: Apportation, Shape Earth
spellSource: Magic
spellReference: M145
spellLink: [[Magic.pdf#page=147&search=Light Tread]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic.pdf#page=147&search=Light Tread|Spell Link]]

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