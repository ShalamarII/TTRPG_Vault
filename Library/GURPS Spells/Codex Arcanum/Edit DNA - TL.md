---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Edit DNAu002FTL
spellCollege: [Technological]
spellDifficulty: 
spellClass: Enchantment
spellResisted: 
spellDuration: '"1 day"'
spellCastingTime: '"10 seconds"'
spellCost: "20 points per character point to be added or subtracted."
spellMaintenance: "half to maintain"
spellPrerequisites: [Magery, Regeneration]
spellPrereqText: Magery, Regeneration
spellSource: Codex Arcanum
spellReference: GOCA513
spellLink: [[Codex Arcanum.pdf#page=513&search=Edit DNAu002FTL]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=513&search=Edit DNAu002FTL|Spell Link]]

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