---
tags:
  - Spell
  - SpellsAsMagic
spellID: p6pJUe0eKgO3Oeslo 
spellName: Transform Other (@Race@)
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: Will
spellDuration: '"1 hr"'
spellCastingTime: '"2 min"'
spellCost: "Varies"
spellMaintenance: "Varies"
spellPrerequisites: [Transform Body (@race@), Shapeshift Others, ]
spellPrereqText: Transform Body (@race@), Shapeshift Others
spellSource: Magic
spellReference: M43
spellLink: [[Magic.pdf#page=45&search=Transform Other (@Race@)]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=45&search=Transform Other (@Race@)|Spell Link]]

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