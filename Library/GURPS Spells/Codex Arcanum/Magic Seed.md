---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Magic Seed
spellCollege: [Plant]
spellDifficulty: 
spellClass: Enchantment
spellResisted: 
spellDuration: '"1 minute."'
spellCastingTime: '"10 seconds"'
spellCost: "3 per foot of height and/or hex of area the plant will cover"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Magery, Create Plant, Link]
spellPrereqText: Magery, Create Plant, Link
spellSource: Codex Arcanum
spellReference: GOCA468
spellLink: [[Codex Arcanum.pdf#page=468&search=Magic Seed]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=468&search=Magic Seed|Spell Link]]

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