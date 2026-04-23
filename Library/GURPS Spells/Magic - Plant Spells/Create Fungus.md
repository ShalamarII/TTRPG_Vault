---
tags:
  - Spell
  - SpellsAsMagic
spellID: pc_04BJ91mBFUcp1V 
spellName: Create Fungus
spellCollege: [Fungus]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"Varies"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Fungus Growth, Magery 1, Fungus 1, ]
spellPrereqText: Fungus Growth, Magery 1, Fungus 1
spellSource: Magic - Plant Spells
spellReference: MPS17
spellLink: [[Magic - Plant Spells.pdf#page=17&search=Create Fungus]]
spellPoints: 1
spellTags: Fungus
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=17&search=Create Fungus|Spell Link]]

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