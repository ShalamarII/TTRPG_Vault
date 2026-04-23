---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Dream Beast
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 hour “dream time”."'
spellCastingTime: '"10 seconds"'
spellCost: "1 per 100 lbs. that the animal would weigh in the “real world”."
spellMaintenance: "half to maintain"
spellPrerequisites: [Dream Travel]
spellPrereqText: Dream Travel
spellSource: Codex Arcanum
spellReference: GOCA85
spellLink: [[Codex Arcanum.pdf#page=85&search=Dream Beast]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=85&search=Dream Beast|Spell Link]]

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