---
tags:
  - Spell
  - SpellsAsMagic
spellID: pTVvpS8vyb6B_560Q 
spellName: Druid's Panacea
spellCollege: [Plant]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"10 Min."'
spellCost: "1-3 once per day"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Plant 3, Plant Empathy, Body Of Wood, ]
spellPrereqText: Magery 3, Plant 3, Plant Empathy, Body Of Wood
spellSource: Magic - Plant Spells
spellReference: MPS12
spellLink: [[Magic - Plant Spells.pdf#page=12&search=Druid's Panacea]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=12&search=Druid's Panacea|Spell Link]]

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