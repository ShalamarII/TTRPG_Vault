---
tags:
  - Spell
  - SpellsAsMagic
spellID: p9ss0AJPwazGj_BFW 
spellName: Distant Blow
spellCollege: [Movement]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"5 sec"'
spellCastingTime: '"3 sec"'
spellCost: "3"
spellMaintenance: "3"
spellPrerequisites: [Magery 2, Movement 2, Apportation, ]
spellPrereqText: Magery 2, Movement 2, Apportation
spellSource: Magic
spellReference: M144
spellLink: [[Magic.pdf#page=146&search=Distant Blow]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic.pdf#page=146&search=Distant Blow|Spell Link]]

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