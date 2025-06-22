---
tags:
  - Spell
  - SpellsAsMagic
spellID: pFLbwHexfOQJq9yzN 
spellName: Swamp Rot
spellCollege: [Plant]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "11"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Plant 3, Body Of Slime, ]
spellPrereqText: Magery 3, Plant 3, Body Of Slime
spellSource: Magic - Death Spells
spellReference: MDS19
spellLink: [[Magic - Death Spells.pdf#page=19&search=Swamp Rot]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=19&search=Swamp Rot|Spell Link]]

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