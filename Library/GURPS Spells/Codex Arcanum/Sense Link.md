---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Sense Link
spellCollege: [Knowledge]
spellDifficulty: 
spellClass: Information
spellResisted: 
spellDuration: '"3 seconds (copied pages are permanent)"'
spellCastingTime: '"10 seconds"'
spellCost: "3"
spellMaintenance: ""
spellPrerequisites: [Sense Foes, 3 Knowledge Spells]
spellPrereqText: Sense Foes, 3 Knowledge Spells
spellSource: Codex Arcanum
spellReference: GOCA298
spellLink: [[Codex Arcanum.pdf#page=298&search=Sense Link]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=298&search=Sense Link|Spell Link]]

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