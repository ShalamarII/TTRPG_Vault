---
tags:
  - Spell
  - SpellsAsMagic
spellID: pE2E3G1LGHaOa0utw 
spellName: Tree Bark Armor
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 Min."'
spellCastingTime: '"4 Sec."'
spellCost: "4"
spellMaintenance: "3"
spellPrerequisites: [Magery 1, Plant 1, Essential Wood, Shape Plant, ]
spellPrereqText: Magery 1, Plant 1, Essential Wood, Shape Plant
spellSource: Magic - Plant Spells
spellReference: MPS20
spellLink: [[Magic - Plant Spells.pdf#page=20&search=Tree Bark Armor]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=20&search=Tree Bark Armor|Spell Link]]

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