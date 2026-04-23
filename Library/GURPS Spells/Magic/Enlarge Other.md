---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVmqaQG9R9Ek9ybS0 
spellName: Enlarge Other
spellCollege: [Body Control]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "2 per +1 SM"
spellMaintenance: "Same"
spellPrerequisites: [Magery 3, Body Control 3, Enlarge, ]
spellPrereqText: Magery 3, Body Control 3, Enlarge
spellSource: Magic
spellReference: M43
spellLink: [[Magic.pdf#page=45&search=Enlarge Other]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=45&search=Enlarge Other|Spell Link]]

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