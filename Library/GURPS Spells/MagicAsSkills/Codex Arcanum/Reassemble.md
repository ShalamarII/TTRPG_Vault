---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Reassemble
spellCollege: [Gate]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"10"'
spellCastingTime: '"10 seconds"'
spellCost: "2 for up to 10 lbs. Of material affected"
spellMaintenance: "or 6 per hex, same to maintain"
spellPrerequisites: [Reverse]
spellPrereqText: Reverse
spellSource: Codex Arcanum
spellReference: GOCA147
spellLink: [[Codex Arcanum.pdf#page=147&search=Reassemble]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=147&search=Reassemble|Spell Link]]

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