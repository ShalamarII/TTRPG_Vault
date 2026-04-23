---
tags:
  - Spell
  - SpellsAsMagic
spellID: pF5yePHnOMSrrdOC7 
spellName: Divert Teleport
spellCollege: [Gate, Movement]
spellDifficulty: IQ/VH
spellClass: Blocking
spellResisted: Subject spell
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Gate 3, Trace Teleport, ]
spellPrereqText: Magery 3, Gate 3, Trace Teleport
spellSource: Magic
spellReference: M84
spellLink: [[Magic.pdf#page=86&search=Divert Teleport]]
spellPoints: 1
spellTags: Gate, Movement
spellWeapons: 
---

 [[Magic.pdf#page=86&search=Divert Teleport|Spell Link]]

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