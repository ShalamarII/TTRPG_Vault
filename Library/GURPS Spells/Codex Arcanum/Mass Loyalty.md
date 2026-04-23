---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Mass Loyalty
spellCollege: [Mind Control]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"1 Hour."'
spellCastingTime: '"1second per 5 energy points used to cast this spell."'
spellCost: "2 to cast"
spellMaintenance: "same to maintain"
spellPrerequisites: [Loyalty.]
spellPrereqText: Loyalty.
spellSource: Codex Arcanum
spellReference: GOCA393
spellLink: [[Codex Arcanum.pdf#page=393&search=Mass Loyalty]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=393&search=Mass Loyalty|Spell Link]]

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