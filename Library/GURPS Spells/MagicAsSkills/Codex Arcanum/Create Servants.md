---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Create Servants
spellCollege: [Illusion and Creation]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"1 Minute."'
spellCastingTime: '"6 seconds per hex of range."'
spellCost: "3 to cast"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Magery, Create Servant, 10 Illusion and Creation spells.]
spellPrereqText: Magery, Create Servant, 10 Illusion and Creation spells.
spellSource: Codex Arcanum
spellReference: GOCA261
spellLink: [[Codex Arcanum.pdf#page=261&search=Create Servants]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=261&search=Create Servants|Spell Link]]

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