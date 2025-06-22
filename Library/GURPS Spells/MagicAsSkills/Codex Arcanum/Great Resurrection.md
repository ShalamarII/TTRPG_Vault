---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Great Resurrection
spellCollege: [Healing]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"Until killed again."'
spellCastingTime: '"2 Hours."'
spellCost: "500"
spellMaintenance: "same to maintain"
spellPrerequisites: [Magery 2, Resurrection, 10 other healing spells.]
spellPrereqText: Magery 2, Resurrection, 10 other healing spells.
spellSource: Codex Arcanum
spellReference: GOCA241
spellLink: [[Codex Arcanum.pdf#page=241&search=Great Resurrection]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=241&search=Great Resurrection|Spell Link]]

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