---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Learn Spell
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"8 hours or until subject wakes."'
spellCastingTime: '"10 hours/day for 8 days."'
spellCost: "5 per day from both caster andsubject."
spellMaintenance: "1 to maintain"
spellPrerequisites: [Teaching, Borrow Skill, and Borrow Language]
spellPrereqText: Teaching, Borrow Skill, and Borrow Language
spellSource: Codex Arcanum
spellReference: GOCA83
spellLink: [[Codex Arcanum.pdf#page=83&search=Learn Spell]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=83&search=Learn Spell|Spell Link]]

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