---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Major Gated Weapon
spellCollege: [Gate]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 seconds Casting Cost: 4 points per level;"'
spellCastingTime: '"10 seconds"'
spellCost: "5"
spellMaintenance: "plus 2 points per hex, half to maintain"
spellPrerequisites: [Gated Weapon.]
spellPrereqText: Gated Weapon.
spellSource: Codex Arcanum
spellReference: GOCA144
spellLink: [[Codex Arcanum.pdf#page=144&search=Major Gated Weapon]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=144&search=Major Gated Weapon|Spell Link]]

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