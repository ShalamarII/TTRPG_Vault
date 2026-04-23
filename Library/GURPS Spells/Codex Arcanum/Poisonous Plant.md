---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Poisonous Plant
spellCollege: [Plant]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"1 minute (poison produced and effects of poison are permanent)"'
spellCastingTime: '"10 seconds. This spell can be made permanent for 25 times the Base Cost."'
spellCost: "3"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Itchy Plant]
spellPrereqText: Itchy Plant
spellSource: Codex Arcanum
spellReference: GOCA471
spellLink: [[Codex Arcanum.pdf#page=471&search=Poisonous Plant]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=471&search=Poisonous Plant|Spell Link]]

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