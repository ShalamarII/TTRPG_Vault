---
tags:
  - Spell
  - SpellsAsMagic
spellID: pQdc1zbOM5_L8TD94 
spellName: Decapitation
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Semi-permanent"'
spellCastingTime: '"2 sec"'
spellCost: "4"
spellMaintenance: "-"
spellPrerequisites: [Magery 2, Body Control 2, Alter Body, ]
spellPrereqText: Magery 2, Body Control 2, Alter Body
spellSource: Magic
spellReference: M42
spellLink: [[Magic.pdf#page=44&search=Decapitation]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=44&search=Decapitation|Spell Link]]

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