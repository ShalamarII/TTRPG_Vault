---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Necrosculpt
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent."'
spellCastingTime: '"1 minute, multiplied by the number of corpses from which parts were taken to build"'
spellCost: "2 per hex that the creation occupies when standing upright"
spellMaintenance: ""
spellPrerequisites: [Enchant, Zombie, Shape Bone, 3 Necromantic Spells]
spellPrereqText: Enchant, Zombie, Shape Bone, 3 Necromantic Spells
spellSource: Codex Arcanum
spellReference: GOCA437
spellLink: [[Codex Arcanum.pdf#page=437&search=Necrosculpt]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=437&search=Necrosculpt|Spell Link]]

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