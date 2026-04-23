---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Weather Stasis
spellCollege: [Earth]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"6 hours"'
spellCastingTime: '"10 minutes."'
spellCost: "1/20. Cost to maintain doubles for each six hour period. The cost is doubled again for"
spellMaintenance: ""
spellPrerequisites: [Magery, 5 spells each from the College of Elemental Air and Water.]
spellPrereqText: Magery, 5 spells each from the College of Elemental Air and Water.
spellSource: Codex Arcanum
spellReference: GOCA172
spellLink: [[Codex Arcanum.pdf#page=172&search=Weather Stasis]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=172&search=Weather Stasis|Spell Link]]

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