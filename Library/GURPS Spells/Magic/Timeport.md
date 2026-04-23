---
tags:
  - Spell
  - SpellsAsMagic
spellID: pS5-9gqS3D7ZgAdcS 
spellName: Timeport
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Teleport, Magery 3, Gate 3, ]
spellPrereqText: Teleport, Magery 3, Gate 3
spellSource: Magic
spellReference: M81
spellLink: [[Magic.pdf#page=83&search=Timeport]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=83&search=Timeport|Spell Link]]

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