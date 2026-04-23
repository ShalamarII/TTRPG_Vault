---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Pliable Magic
spellCollege: [Making and Breaking]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 minutes"'
spellCastingTime: '""'
spellCost: "1 point per pound of material"
spellMaintenance: "1 to maintain"
spellPrerequisites: [4 Making and Breaking spells]
spellPrereqText: 4 Making and Breaking spells
spellSource: Codex Arcanum
spellReference: GOCA333
spellLink: [[Codex Arcanum.pdf#page=333&search=Pliable Magic]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=333&search=Pliable Magic|Spell Link]]

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