---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Predict Flood
spellCollege: [Water]
spellDifficulty: 
spellClass: Information
spellResisted: 
spellDuration: '"1 hour"'
spellCastingTime: '"1 minute"'
spellCost: "3 points"
spellMaintenance: "2 to maintain"
spellPrerequisites: [3 Water Spells]
spellPrereqText: 3 Water Spells
spellSource: Codex Arcanum
spellReference: GOCA219
spellLink: [[Codex Arcanum.pdf#page=219&search=Predict Flood]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=219&search=Predict Flood|Spell Link]]

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