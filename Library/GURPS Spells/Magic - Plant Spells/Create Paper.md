---
tags:
  - Spell
  - SpellsAsMagic
spellID: pY6JimIP7bghn4VjL 
spellName: Create Paper
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"4 Min."'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Magery 2, Plant 2, Heal Plant, ]
spellPrereqText: Magery 2, Plant 2, Heal Plant
spellSource: Magic - Plant Spells
spellReference: MPS12
spellLink: [[Magic - Plant Spells.pdf#page=12&search=Create Paper]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=12&search=Create Paper|Spell Link]]

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