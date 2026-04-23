---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Planar Summons
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"1 hour or more."'
spellCastingTime: '"5 minutes"'
spellCost: "20"
spellMaintenance: ""
spellPrerequisites: [Magery, and at least 1 spell from each of 10 different colleges.]
spellPrereqText: Magery, and at least 1 spell from each of 10 different colleges.
spellSource: Codex Arcanum
spellReference: GOCA439
spellLink: [[Codex Arcanum.pdf#page=439&search=Planar Summons]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=439&search=Planar Summons|Spell Link]]

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