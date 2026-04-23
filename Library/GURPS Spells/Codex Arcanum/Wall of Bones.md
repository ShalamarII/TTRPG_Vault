---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Wall of Bones
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"1 minute."'
spellCastingTime: '"1 second per point of energy put into the spell"'
spellCost: "2 per hex to cast"
spellMaintenance: "same to maintain"
spellPrerequisites: [Control Zombie, 4 other Necromantic spells]
spellPrereqText: Control Zombie, 4 other Necromantic spells
spellSource: Codex Arcanum
spellReference: GOCA453
spellLink: [[Codex Arcanum.pdf#page=453&search=Wall of Bones]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=453&search=Wall of Bones|Spell Link]]

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