---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Improve Gem
spellCollege: [Earth]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '"1 minute"'
spellCost: "3 for 10% improvement"
spellMaintenance: ""
spellPrerequisites: [Magery, Shape Earth, 3 other earth spells.]
spellPrereqText: Magery, Shape Earth, 3 other earth spells.
spellSource: Codex Arcanum
spellReference: GOCA182
spellLink: [[Codex Arcanum.pdf#page=182&search=Improve Gem]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=182&search=Improve Gem|Spell Link]]

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