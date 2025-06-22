---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Worldwalk
spellCollege: [Gate]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"10 seconds"'
spellCastingTime: '"3d6 days, minus skill, plus the number of people being transported."'
spellCost: "0"
spellMaintenance: "10 to maintain"
spellPrerequisites: [Native of 'mirror' dimension or Gate]
spellPrereqText: Native of 'mirror' dimension or Gate
spellSource: Codex Arcanum
spellReference: GOCA153
spellLink: [[Codex Arcanum.pdf#page=153&search=Worldwalk]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=153&search=Worldwalk|Spell Link]]

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