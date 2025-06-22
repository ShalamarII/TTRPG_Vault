---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Mass Zombie
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"The Zombies remain animated until destroyed."'
spellCastingTime: '"1 minute per hex of radius"'
spellCost: "7. Minimum radius 2 hexes."
spellMaintenance: ""
spellPrerequisites: [Zombie, and two or more levels of either Charisma or Strong Will.]
spellPrereqText: Zombie, and two or more levels of either Charisma or Strong Will.
spellSource: Codex Arcanum
spellReference: GOCA436
spellLink: [[Codex Arcanum.pdf#page=436&search=Mass Zombie]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=436&search=Mass Zombie|Spell Link]]

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