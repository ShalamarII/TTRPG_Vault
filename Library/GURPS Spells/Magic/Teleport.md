---
tags:
  - Spell
  - SpellsAsMagic
spellID: p1VQXxbWhD8bnPJ7Y 
spellName: Teleport
spellCollege: [Gate, Movement]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Hawk Flight, at least 13 IQ, 0 Spell(s) from 10 Colleges, ]
spellPrereqText: Hawk Flight, at least 13 IQ, 0 Spell(s) from 10 Colleges
spellSource: Magic
spellReference: M147
spellLink: [[Magic.pdf#page=149&search=Teleport]]
spellPoints: 1
spellTags: Gate, Movement
spellWeapons: 
---

 [[Magic.pdf#page=149&search=Teleport|Spell Link]]

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