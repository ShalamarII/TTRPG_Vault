---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Leaping Flames
spellCollege: [Fire]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Instantaneous Base Cost: 1 per 10 feet of distance from the flame source hex."'
spellCastingTime: '""'
spellCost: "1 per 10 feet of distance from the flame source hex."
spellMaintenance: ""
spellPrerequisites: [Shape Fire]
spellPrereqText: Shape Fire
spellSource: Codex Arcanum
spellReference: GOCA205
spellLink: [[Codex Arcanum.pdf#page=205&search=Leaping Flames]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=205&search=Leaping Flames|Spell Link]]

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