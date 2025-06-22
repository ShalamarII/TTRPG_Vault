---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Earth Wave
spellCollege: [Earth]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"10 seconds"'
spellCastingTime: '"1 second per point of Base Cost."'
spellCost: "4 per hex (minimum of 2 hexes)"
spellMaintenance: "same to maintain"
spellPrerequisites: [Magery 2, Shape Earth, 10 other Earth spells.]
spellPrereqText: Magery 2, Shape Earth, 10 other Earth spells.
spellSource: Codex Arcanum
spellReference: GOCA179
spellLink: [[Codex Arcanum.pdf#page=179&search=Earth Wave]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=179&search=Earth Wave|Spell Link]]

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