---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Obscure Terrain
spellCollege: [Protection & Warning]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"1 day"'
spellCastingTime: '"1 minute"'
spellCost: "3 per quarter mile radius from the mage’s position. An area can be permanently"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Scry Ward]
spellPrereqText: Scry Ward
spellSource: Codex Arcanum
spellReference: GOCA524
spellLink: [[Codex Arcanum.pdf#page=524&search=Obscure Terrain]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=524&search=Obscure Terrain|Spell Link]]

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