---
tags:
  - Spell
  - SpellsAsMagic
spellID: p7tXTU_YacUnko6hE 
spellName: Planar Visit (@plane@)
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"30 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Projection, Planar Summons (@plane@), Magery 2, Gate 2, ]
spellPrereqText: Projection, Planar Summons (@plane@), Magery 2, Gate 2
spellSource: Magic
spellReference: M82
spellLink: [[Magic.pdf#page=84&search=Planar Visit (@plane@)]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=84&search=Planar Visit (@plane@)|Spell Link]]

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