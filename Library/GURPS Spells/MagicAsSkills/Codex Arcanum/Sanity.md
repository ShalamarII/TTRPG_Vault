---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Sanity
spellCollege: [Mind Control]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 minutes"'
spellCastingTime: '"1 minute"'
spellCost: "4"
spellMaintenance: "same to maintain"
spellPrerequisites: [Magery, Bravery, Forgetfulness]
spellPrereqText: Magery, Bravery, Forgetfulness
spellSource: Codex Arcanum
spellReference: GOCA401
spellLink: [[Codex Arcanum.pdf#page=401&search=Sanity]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=401&search=Sanity|Spell Link]]

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