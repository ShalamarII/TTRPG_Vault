---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Decrease Mana Level
spellCollege: [Meta]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 minute Base Cost: 10 per hex for a one-level decrease (e.g. 'Normal' to 'Low'), 25 per"'
spellCastingTime: '"10 seconds"'
spellCost: "10 per hex for a one-level decrease (e.g. 'Normal' to 'Low')"
spellMaintenance: "same to maintain"
spellPrerequisites: [Magery, Drain Mana]
spellPrereqText: Magery, Drain Mana
spellSource: Codex Arcanum
spellReference: GOCA350
spellLink: [[Codex Arcanum.pdf#page=350&search=Decrease Mana Level]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=350&search=Decrease Mana Level|Spell Link]]

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