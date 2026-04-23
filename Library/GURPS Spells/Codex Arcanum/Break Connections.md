---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Break Connections
spellCollege: [Meta]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 month for body parts, permanent for objects."'
spellCastingTime: '"10 seconds."'
spellCost: "1 for the subject's hair"
spellMaintenance: "3 to maintain"
spellPrerequisites: [Seek Ley Line, Break Powerstone Tap, Magery 3, Tap Ley Line]
spellPrereqText: Seek Ley Line, Break Powerstone Tap, Magery 3, Tap Ley Line
spellSource: Codex Arcanum
spellReference: GOCA345
spellLink: [[Codex Arcanum.pdf#page=345&search=Break Connections]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=345&search=Break Connections|Spell Link]]

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