---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Divine Resurrection
spellCollege: [Healing]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"Until killed again."'
spellCastingTime: '"8 hours."'
spellCost: "1000"
spellMaintenance: ""
spellPrerequisites: [Great Resurrection, Planar Summons, at least 2 Spells from each of the 15 colleges.]
spellPrereqText: Great Resurrection, Planar Summons, at least 2 Spells from each of the 15 colleges.
spellSource: Codex Arcanum
spellReference: GOCA239
spellLink: [[Codex Arcanum.pdf#page=239&search=Divine Resurrection]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=239&search=Divine Resurrection|Spell Link]]

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