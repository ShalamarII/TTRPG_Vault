---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Exploding Ice Sphere
spellCollege: [Water]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 second per point of energy put into the spell."'
spellCost: "1 per die of damage"
spellMaintenance: ""
spellPrerequisites: [Magery, Ice Sphere.]
spellPrereqText: Magery, Ice Sphere.
spellSource: Codex Arcanum
spellReference: GOCA226
spellLink: [[Codex Arcanum.pdf#page=226&search=Exploding Ice Sphere]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=226&search=Exploding Ice Sphere|Spell Link]]

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