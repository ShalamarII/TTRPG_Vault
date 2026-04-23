---
tags:
  - Spell
  - SpellsAsMagic
spellID: p4jXBEdrPoIGcgQQI 
spellName: Enthrall
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: Will
spellDuration: '"1 hr"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "3"
spellPrerequisites: [Forgetfulness, Daze, Slow, ]
spellPrereqText: Forgetfulness, Daze, Slow
spellSource: Magic
spellReference: M139
spellLink: [[Magic.pdf#page=141&search=Enthrall]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=141&search=Enthrall|Spell Link]]

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