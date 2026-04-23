---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Gather Starwater
spellCollege: [Meta]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Variable."'
spellCastingTime: '"Variable."'
spellCost: "10"
spellMaintenance: ""
spellPrerequisites: [Magery 2, one spell from each of 10 different colleges.]
spellPrereqText: Magery 2, one spell from each of 10 different colleges.
spellSource: Codex Arcanum
spellReference: GOCA353
spellLink: [[Codex Arcanum.pdf#page=353&search=Gather Starwater]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=353&search=Gather Starwater|Spell Link]]

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