---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Fire Bug
spellCollege: [Fire]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 hour"'
spellCastingTime: '"1 second per bug."'
spellCost: "1 point per bug. The Duration of the spell can be extended for the same cost."
spellMaintenance: "1 to maintain"
spellPrerequisites: [Shape Fire, Hang Spell]
spellPrereqText: Shape Fire, Hang Spell
spellSource: Codex Arcanum
spellReference: GOCA200
spellLink: [[Codex Arcanum.pdf#page=200&search=Fire Bug]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=200&search=Fire Bug|Spell Link]]

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