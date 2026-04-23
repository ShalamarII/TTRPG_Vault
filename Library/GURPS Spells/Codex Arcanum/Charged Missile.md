---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Charged Missile
spellCollege: [Electricity]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"10 seconds (damage is instantaneous)."'
spellCastingTime: '"1 second per point of energy."'
spellCost: "1 per 1d-1 damage."
spellMaintenance: "3 to maintain"
spellPrerequisites: [Electric Weapon]
spellPrereqText: Electric Weapon
spellSource: Codex Arcanum
spellReference: GOCA6
spellLink: [[Codex Arcanum.pdf#page=6&search=Charged Missile]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=6&search=Charged Missile|Spell Link]]

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