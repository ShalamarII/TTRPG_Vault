---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Change Liquid
spellCollege: [Water]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '""'
spellCost: "1 per gallon. Double costs if the material created is rare or valuable."
spellMaintenance: ""
spellPrerequisites: [Magery, Create Water.]
spellPrereqText: Magery, Create Water.
spellSource: Codex Arcanum
spellReference: GOCA215
spellLink: [[Codex Arcanum.pdf#page=215&search=Change Liquid]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=215&search=Change Liquid|Spell Link]]

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