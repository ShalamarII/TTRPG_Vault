---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Blood Bank
spellCollege: [Food]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Special"'
spellCastingTime: '"10 Seconds."'
spellCost: "1 per 2 HT of blood drunk."
spellMaintenance: ""
spellPrerequisites: [Preserve Food, Sterilize, Steal Health.]
spellPrereqText: Preserve Food, Sterilize, Steal Health.
spellSource: Codex Arcanum
spellReference: GOCA109
spellLink: [[Codex Arcanum.pdf#page=109&search=Blood Bank]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=109&search=Blood Bank|Spell Link]]

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