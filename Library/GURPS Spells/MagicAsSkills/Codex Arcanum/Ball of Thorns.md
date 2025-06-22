---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Ball of Thorns
spellCollege: [Plant]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"1 to 5 seconds, as specified by the caster."'
spellCastingTime: '"2 seconds"'
spellCost: "3 points"
spellMaintenance: "3 to maintain"
spellPrerequisites: [Shape Plant]
spellPrereqText: Shape Plant
spellSource: Codex Arcanum
spellReference: GOCA458
spellLink: [[Codex Arcanum.pdf#page=458&search=Ball of Thorns]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=458&search=Ball of Thorns|Spell Link]]

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