---
tags:
  - Spell
  - SpellsAsMagic
spellID: pCqCVOnXuGOBRIC0A 
spellName: Restore
spellCollege: [Making & Breaking]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 min"'
spellCastingTime: '"3 sec"'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [Find Weakness, Simple Illusion, ]
spellPrereqText: Find Weakness, Simple Illusion
spellSource: Magic
spellReference: M116
spellLink: [[Magic.pdf#page=118&search=Restore]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: 
---

 [[Magic.pdf#page=118&search=Restore|Spell Link]]

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