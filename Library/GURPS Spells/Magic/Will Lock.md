---
tags:
  - Spell
  - SpellsAsMagic
spellID: puiR1_eMgR-1W4e1m 
spellName: Will Lock
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: (ST+Will)/2
spellDuration: '"1 day"'
spellCastingTime: '"Varies"'
spellCost: "3"
spellMaintenance: "-"
spellPrerequisites: [Emotion Control, ]
spellPrereqText: Emotion Control
spellSource: Magic
spellReference: M138
spellLink: [[Magic.pdf#page=140&search=Will Lock]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=140&search=Will Lock|Spell Link]]

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