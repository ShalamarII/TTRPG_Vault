---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Autofire Missile
spellCollege: [Meta]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"10 seconds, or one spell, whichever is less."'
spellCastingTime: '"1 second."'
spellCost: "2 to12. Each fatigue point buys 1d worth of Missiles. The caster decides on the size of"
spellMaintenance: ""
spellPrerequisites: [Magery 3, Simulcast, Great Haste, 5 other Metaspells]
spellPrereqText: Magery 3, Simulcast, Great Haste, 5 other Metaspells
spellSource: Codex Arcanum
spellReference: GOCA343
spellLink: [[Codex Arcanum.pdf#page=343&search=Autofire Missile]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=343&search=Autofire Missile|Spell Link]]

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