---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Foul Taste
spellCollege: [Animal]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 minutes"'
spellCastingTime: '"2 seconds"'
spellCost: "2"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Beast Soother]
spellPrereqText: Beast Soother
spellSource: Codex Arcanum
spellReference: GOCA21
spellLink: [[Codex Arcanum.pdf#page=21&search=Foul Taste]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=21&search=Foul Taste|Spell Link]]

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