---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Chain Missile
spellCollege: [Meta]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"10 seconds, plus the Duration of the Missile."'
spellCastingTime: '"1 second per point of energy."'
spellCost: "1 per point of damage in the missile spell."
spellMaintenance: ""
spellPrerequisites: [Magery, Link, 3 missile spell plus the missile spell to be chained.]
spellPrereqText: Magery, Link, 3 missile spell plus the missile spell to be chained.
spellSource: Codex Arcanum
spellReference: GOCA346
spellLink: [[Codex Arcanum.pdf#page=346&search=Chain Missile]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=346&search=Chain Missile|Spell Link]]

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