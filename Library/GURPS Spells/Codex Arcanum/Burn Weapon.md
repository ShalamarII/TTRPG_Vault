---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Burn Weapon
spellCollege: [Fire]
spellDifficulty: 
spellClass: Blocking
spellResisted: 
spellDuration: '"1 attack"'
spellCastingTime: '"10 seconds"'
spellCost: "1 to 3 points"
spellMaintenance: ""
spellPrerequisites: [Burning Touch]
spellPrereqText: Burning Touch
spellSource: Codex Arcanum
spellReference: GOCA199
spellLink: [[Codex Arcanum.pdf#page=199&search=Burn Weapon]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=199&search=Burn Weapon|Spell Link]]

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