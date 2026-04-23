---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Direct
spellCollege: [Movement]
spellDifficulty: 
spellClass: Information
spellResisted: 
spellDuration: '"1 minute"'
spellCastingTime: '""'
spellCost: "2 points"
spellMaintenance: "to a maximum of 3, same to maintain"
spellPrerequisites: [Teleport, Time Travel or Dimension Travel.]
spellPrereqText: Teleport, Time Travel or Dimension Travel.
spellSource: Codex Arcanum
spellReference: GOCA411
spellLink: [[Codex Arcanum.pdf#page=411&search=Direct]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=411&search=Direct|Spell Link]]

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