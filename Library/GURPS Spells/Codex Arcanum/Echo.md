---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Echo
spellCollege: [Sound and Hearing]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"1 minute"'
spellCastingTime: '"3 seconds, the caster must concentrate on the spell for its entire Duration."'
spellCost: "3"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Distort Sound]
spellPrereqText: Distort Sound
spellSource: Codex Arcanum
spellReference: GOCA486
spellLink: [[Codex Arcanum.pdf#page=486&search=Echo]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=486&search=Echo|Spell Link]]

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