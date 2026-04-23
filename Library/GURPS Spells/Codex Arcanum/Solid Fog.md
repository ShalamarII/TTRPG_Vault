---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Solid Fog
spellCollege: [Water]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"1 minute (or longer depending on the surroundings)."'
spellCastingTime: '"2 seconds"'
spellCost: "3 to cast"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Magery, Fog, Shape Air or Shape Water]
spellPrereqText: Magery, Fog, Shape Air or Shape Water
spellSource: Codex Arcanum
spellReference: GOCA230
spellLink: [[Codex Arcanum.pdf#page=230&search=Solid Fog]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=230&search=Solid Fog|Spell Link]]

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