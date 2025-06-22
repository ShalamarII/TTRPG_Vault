---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Predict Eclipse
spellCollege: [Earth]
spellDifficulty: 
spellClass: Information
spellResisted: 
spellDuration: '"10 minutes"'
spellCastingTime: '"5 seconds"'
spellCost: "1"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Predict Weather]
spellPrereqText: Predict Weather
spellSource: Codex Arcanum
spellReference: GOCA172
spellLink: [[Codex Arcanum.pdf#page=172&search=Predict Eclipse]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=172&search=Predict Eclipse|Spell Link]]

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