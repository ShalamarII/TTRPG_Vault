---
tags:
  - Spell
  - SpellsAsMagic
spellID: pPcLDJ01xeoZiwemD 
spellName: Suspend Magery
spellCollege: [Meta]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will+Magery
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "12"
spellMaintenance: "Same"
spellPrerequisites: [2 Spell(s) from 10 Colleges, Magery 2, Meta 2, ]
spellPrereqText: 2 Spell(s) from 10 Colleges, Magery 2, Meta 2
spellSource: Magic
spellReference: M130
spellLink: [[Magic.pdf#page=132&search=Suspend Magery]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=132&search=Suspend Magery|Spell Link]]

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