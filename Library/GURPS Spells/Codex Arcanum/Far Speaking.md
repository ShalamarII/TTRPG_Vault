---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Far Speaking
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 minutes"'
spellCastingTime: '"2 seconds."'
spellCost: "4 to cast"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Magery, Selective Message, Great Voice]
spellPrereqText: Magery, Selective Message, Great Voice
spellSource: Codex Arcanum
spellReference: GOCA68
spellLink: [[Codex Arcanum.pdf#page=68&search=Far Speaking]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=68&search=Far Speaking|Spell Link]]

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