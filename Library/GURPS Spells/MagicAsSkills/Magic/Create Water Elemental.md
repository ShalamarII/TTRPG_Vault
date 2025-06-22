---
tags:
  - Spell
  - SpellsAsMagic
spellID: p4d1FSOf5blX-AgIc 
spellName: Create Water Elemental
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"Special"'
spellCost: "Special"
spellMaintenance: "-"
spellPrerequisites: [Magery 2, Water 2, Control Water Elemental, ]
spellPrereqText: Magery 2, Water 2, Control Water Elemental
spellSource: Magic
spellReference: M28
spellLink: [[Magic.pdf#page=30&search=Create Water Elemental]]
spellPoints: 1
spellTags: Water
spellWeapons: 
---

 [[Magic.pdf#page=30&search=Create Water Elemental|Spell Link]]

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