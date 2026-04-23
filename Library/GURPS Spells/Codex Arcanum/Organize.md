---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Organize
spellCollege: [Making and Breaking]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '"1 minute"'
spellCost: "3 per hex (or objects occupying part of a hex.)"
spellMaintenance: ""
spellPrerequisites: [Gather, 3 Making and Breaking spells.]
spellPrereqText: Gather, 3 Making and Breaking spells.
spellSource: Codex Arcanum
spellReference: GOCA332
spellLink: [[Codex Arcanum.pdf#page=332&search=Organize]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=332&search=Organize|Spell Link]]

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