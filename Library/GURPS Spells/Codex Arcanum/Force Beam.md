---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Force Beam
spellCollege: [Force]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"1 second"'
spellCastingTime: '"1 second per energy point used"'
spellCost: "1 point per die of damage"
spellMaintenance: "same to maintain"
spellPrerequisites: [Poltergeist]
spellPrereqText: Poltergeist
spellSource: Codex Arcanum
spellReference: GOCA126
spellLink: [[Codex Arcanum.pdf#page=126&search=Force Beam]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=126&search=Force Beam|Spell Link]]

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