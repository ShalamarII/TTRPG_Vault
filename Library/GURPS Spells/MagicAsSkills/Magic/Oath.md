---
tags:
  - Spell
  - SpellsAsMagic
spellID: psMVXIC8uUrh9uCFB 
spellName: Oath
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Special
spellDuration: '"Permanent"'
spellCastingTime: '"1 min"'
spellCost: "4"
spellMaintenance: "-"
spellPrerequisites: [Emotion Control, Magery 1, Mind Control 1, ]
spellPrereqText: Emotion Control, Magery 1, Mind Control 1
spellSource: Magic
spellReference: M138
spellLink: [[Magic.pdf#page=140&search=Oath]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=140&search=Oath|Spell Link]]

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