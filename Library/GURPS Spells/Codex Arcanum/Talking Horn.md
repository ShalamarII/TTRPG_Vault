---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Talking Horn
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 minute"'
spellCastingTime: '"10 seconds"'
spellCost: "2 points for 100 hex range (every doubling of cost doubles range). The objects can be"
spellMaintenance: "same to maintain"
spellPrerequisites: [Far-Speaking, Wizard Ear]
spellPrereqText: Far-Speaking, Wizard Ear
spellSource: Codex Arcanum
spellReference: GOCA81
spellLink: [[Codex Arcanum.pdf#page=81&search=Talking Horn]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=81&search=Talking Horn|Spell Link]]

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