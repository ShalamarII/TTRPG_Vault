---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Oathbinding
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent, until oath is fulfilled or ends"'
spellCastingTime: '"Variable."'
spellCost: "2 to 10"
spellMaintenance: "3 to maintain"
spellPrerequisites: [Magery, Gift of Tongues, Borrow Skill]
spellPrereqText: Magery, Gift of Tongues, Borrow Skill
spellSource: Codex Arcanum
spellReference: GOCA75
spellLink: [[Codex Arcanum.pdf#page=75&search=Oathbinding]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=75&search=Oathbinding|Spell Link]]

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