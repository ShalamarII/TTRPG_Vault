---
tags:
  - Spell
  - SpellsAsMagic
spellID: pH5tDGQhnKgcOwivI 
spellName: Rebuild
spellCollege: [Making & Breaking, Technological]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"sec=cost"'
spellCost: "30"
spellMaintenance: "-"
spellPrerequisites: [Schematic, 3 Spell(s) from the Air College, 3 Spell(s) from the Earth College, 3 Spell(s) from the Fire College, 3 Spell(s) from the Water College, Create Object, Repair, Magery 3, Making & Breaking 3, Technological 3, ]
spellPrereqText: Schematic, 3 Spell(s) from the Air College, 3 Spell(s) from the Earth College, 3 Spell(s) from the Fire College, 3 Spell(s) from the Water College, Create Object, Repair, Magery 3, Making & Breaking 3, Technological 3
spellSource: Magic
spellReference: M177
spellLink: [[Magic.pdf#page=179&search=Rebuild]]
spellPoints: 1
spellTags: Machine, Making & Breaking, Technological
spellWeapons: 
---

 [[Magic.pdf#page=179&search=Rebuild|Spell Link]]

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