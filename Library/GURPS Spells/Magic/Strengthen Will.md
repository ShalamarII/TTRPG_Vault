---
tags:
  - Spell
  - SpellsAsMagic
spellID: pxTL1i8yfo3DzPPVz 
spellName: Strengthen Will
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1/pt of Will increase"
spellMaintenance: "Half"
spellPrerequisites: [6 Spell(s) from the Mind Control College, Magery 1, Mind Control 1, ]
spellPrereqText: 6 Spell(s) from the Mind Control College, Magery 1, Mind Control 1
spellSource: Magic
spellReference: M136
spellLink: [[Magic.pdf#page=138&search=Strengthen Will]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=138&search=Strengthen Will|Spell Link]]

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