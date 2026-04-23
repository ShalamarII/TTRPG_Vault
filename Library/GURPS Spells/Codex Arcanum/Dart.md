---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Dart
spellCollege: [Plant]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 second per energy point"'
spellCost: "1 to 3 points (1 point per 1d6-1 damage done)."
spellMaintenance: ""
spellPrerequisites: [Create Plant]
spellPrereqText: Create Plant
spellSource: Codex Arcanum
spellReference: GOCA462
spellLink: [[Codex Arcanum.pdf#page=462&search=Dart]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=462&search=Dart|Spell Link]]

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