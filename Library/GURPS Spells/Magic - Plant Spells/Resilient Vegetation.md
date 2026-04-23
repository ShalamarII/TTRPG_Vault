---
tags:
  - Spell
  - SpellsAsMagic
spellID: p_YRyV2MkrcQiOzhz 
spellName: Resilient Vegetation
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 Min."'
spellCastingTime: '"1 Min."'
spellCost: "1"
spellMaintenance: "Same"
spellPrerequisites: [Magery 1, Plant 1, Shape Plant, ]
spellPrereqText: Magery 1, Plant 1, Shape Plant
spellSource: Magic - Plant Spells
spellReference: MPS17
spellLink: [[Magic - Plant Spells.pdf#page=17&search=Resilient Vegetation]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=17&search=Resilient Vegetation|Spell Link]]

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