---
tags:
  - Spell
  - SpellsAsMagic
spellID: p5_96Y5INMiaK7UFC 
spellName: Searching Roots
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Information
spellResisted: undefined
spellDuration: '"10 Sec."'
spellCastingTime: '"5 Min."'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [Magery 2, Plant 2, Animate Plant, ]
spellPrereqText: Magery 2, Plant 2, Animate Plant
spellSource: Magic - Plant Spells
spellReference: MPS18
spellLink: [[Magic - Plant Spells.pdf#page=18&search=Searching Roots]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=18&search=Searching Roots|Spell Link]]

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