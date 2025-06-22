---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBW4SdfDcW4RXNQa0 
spellName: Coma
spellCollege: [Mind Control]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"3 sec"'
spellCost: "11"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Mind Control 3, Lesser Geas, Sleep, ]
spellPrereqText: Magery 3, Mind Control 3, Lesser Geas, Sleep
spellSource: Magic - Death Spells
spellReference: MDS17
spellLink: [[Magic - Death Spells.pdf#page=17&search=Coma]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=17&search=Coma|Spell Link]]

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