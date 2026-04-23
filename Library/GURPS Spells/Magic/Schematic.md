---
tags:
  - Spell
  - SpellsAsMagic
spellID: pDyJ0cVMq3LPfMBc1 
spellName: Schematic
spellCollege: [Knowledge, Technological]
spellDifficulty: IQ/VH
spellClass: Info
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "5+1/ton"
spellMaintenance: "Half"
spellPrerequisites: [Reveal Function, History, ]
spellPrereqText: Reveal Function, History
spellSource: Magic
spellReference: M177
spellLink: [[Magic.pdf#page=179&search=Schematic]]
spellPoints: 1
spellTags: Knowledge, Machine, Technological
spellWeapons: 
---

 [[Magic.pdf#page=179&search=Schematic|Spell Link]]

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