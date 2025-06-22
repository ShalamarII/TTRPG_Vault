---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Preserve
spellCollege: [Making and Breaking]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"10 years"'
spellCastingTime: '""'
spellCost: "3 per hex or 10 lbs. of material to be preserved. (Each additional casting adds 10 more"
spellMaintenance: ""
spellPrerequisites: [Repair]
spellPrereqText: Repair
spellSource: Codex Arcanum
spellReference: GOCA334
spellLink: [[Codex Arcanum.pdf#page=334&search=Preserve]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=334&search=Preserve|Spell Link]]

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