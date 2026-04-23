---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Obscure Trail
spellCollege: [Plant]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"Permanent.)"'
spellCastingTime: '"10 seconds. An area can be permanently enchanted with this spell for 25 times the"'
spellCost: "3"
spellMaintenance: "same to maintain"
spellPrerequisites: [Pass Without Trace]
spellPrereqText: Pass Without Trace
spellSource: Codex Arcanum
spellReference: GOCA469
spellLink: [[Codex Arcanum.pdf#page=469&search=Obscure Trail]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=469&search=Obscure Trail|Spell Link]]

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