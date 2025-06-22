---
tags:
  - Spell
  - SpellsAsMagic
spellID: pnI5hjKcSyTCYNlVH 
spellName: Suspend Time
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: IQ
spellDuration: '"1 day"'
spellCastingTime: '"5 min"'
spellCost: "5"
spellMaintenance: "Same"
spellPrerequisites: [Slow Time, Magery 3, Gate 3, ]
spellPrereqText: Slow Time, Magery 3, Gate 3
spellSource: Magic
spellReference: M86
spellLink: [[Magic.pdf#page=88&search=Suspend Time]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=88&search=Suspend Time|Spell Link]]

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