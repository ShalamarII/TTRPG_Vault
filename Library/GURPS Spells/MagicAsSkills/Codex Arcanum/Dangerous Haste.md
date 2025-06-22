---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Dangerous Haste
spellCollege: [Movement]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Instant"'
spellCastingTime: '"1 second"'
spellCost: "1 to 3 1d6 per point of energy. Spell also does 2 fatigue per energy point to subject."
spellMaintenance: ""
spellPrerequisites: [Great Haste, Spasm, Fatigue, at least 4 Movement or Body Control spells]
spellPrereqText: Great Haste, Spasm, Fatigue, at least 4 Movement or Body Control spells
spellSource: Codex Arcanum
spellReference: GOCA411
spellLink: [[Codex Arcanum.pdf#page=411&search=Dangerous Haste]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=411&search=Dangerous Haste|Spell Link]]

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