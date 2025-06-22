---
tags:
  - Spell
  - SpellsAsMagic
spellID: pfzKmPffJeOPUV_YU 
spellName: Fascinate
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Regular or Blocking
spellResisted: Will
spellDuration: '"Indefinite"'
spellCastingTime: '"1 sec"'
spellCost: "4"
spellMaintenance: "-"
spellPrerequisites: [Daze, ]
spellPrereqText: Daze
spellSource: Magic
spellReference: M135
spellLink: [[Magic.pdf#page=137&search=Fascinate]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=137&search=Fascinate|Spell Link]]

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