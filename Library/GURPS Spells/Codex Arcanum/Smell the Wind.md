---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Smell the Wind
spellCollege: [Earth]
spellDifficulty: 
spellClass: Information
spellResisted: 
spellDuration: '"1 minute"'
spellCastingTime: '"10 minutes"'
spellCost: "5"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Magery, Divination]
spellPrereqText: Magery, Divination
spellSource: Codex Arcanum
spellReference: GOCA167
spellLink: [[Codex Arcanum.pdf#page=167&search=Smell the Wind]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=167&search=Smell the Wind|Spell Link]]

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