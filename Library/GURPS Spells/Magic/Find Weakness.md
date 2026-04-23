---
tags:
  - Spell
  - SpellsAsMagic
spellID: prf_KTckIQMDPjUhw 
spellName: Find Weakness
spellCollege: [Making & Breaking]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"2 sec"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [1 Spell(s) from the Air College, 1 Spell(s) from the Fire College, 1 Spell(s) from the Water College, 1 Spell(s) from the Earth College, ]
spellPrereqText: 1 Spell(s) from the Air College, 1 Spell(s) from the Fire College, 1 Spell(s) from the Water College, 1 Spell(s) from the Earth College
spellSource: Magic
spellReference: M116
spellLink: [[Magic.pdf#page=118&search=Find Weakness]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: 
---

 [[Magic.pdf#page=118&search=Find Weakness|Spell Link]]

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