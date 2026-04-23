---
tags:
  - Spell
  - SpellsAsMagic
spellID: prL3JiCAx9DVbpFPt 
spellName: Miniaturize Plant
spellCollege: [Plant]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 Min."'
spellCastingTime: '"30 Sec."'
spellCost: "1"
spellMaintenance: "1 / Min."
spellPrerequisites: [Magery 2, Plant 2, Reverse Plant Growth, ]
spellPrereqText: Magery 2, Plant 2, Reverse Plant Growth
spellSource: Magic - Plant Spells
spellReference: MPS16
spellLink: [[Magic - Plant Spells.pdf#page=16&search=Miniaturize Plant]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=16&search=Miniaturize Plant|Spell Link]]

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