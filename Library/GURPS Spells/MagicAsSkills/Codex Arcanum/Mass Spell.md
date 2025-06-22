---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Mass Spell
spellCollege: [Meta]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"10 seconds"'
spellCastingTime: '"5 seconds"'
spellCost: "8"
spellMaintenance: ""
spellPrerequisites: [Magery 2, 6 Other Metaspells.]
spellPrereqText: Magery 2, 6 Other Metaspells.
spellSource: Codex Arcanum
spellReference: GOCA359
spellLink: [[Codex Arcanum.pdf#page=359&search=Mass Spell]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=359&search=Mass Spell|Spell Link]]

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