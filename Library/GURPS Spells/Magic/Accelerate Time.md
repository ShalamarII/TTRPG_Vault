---
tags:
  - Spell
  - SpellsAsMagic
spellID: pG4OKA-9z-K5Dr9De 
spellName: Accelerate Time
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: Special
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "Varies"
spellMaintenance: "Varies"
spellPrerequisites: [2 Spell(s) from 10 Colleges, at least 13 IQ, Magery 2, Gate 2, ]
spellPrereqText: 2 Spell(s) from 10 Colleges, at least 13 IQ, Magery 2, Gate 2
spellSource: Magic
spellReference: M86
spellLink: [[Magic.pdf#page=88&search=Accelerate Time]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=88&search=Accelerate Time|Spell Link]]

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