---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Self-Destruct
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Enchantment
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '"1 minute per point of fatigue spent"'
spellCost: "50 points"
spellMaintenance: ""
spellPrerequisites: [Enchant, Ruin, Limit]
spellPrereqText: Enchant, Ruin, Limit
spellSource: Codex Arcanum
spellReference: GOCA102
spellLink: [[Codex Arcanum.pdf#page=102&search=Self-Destruct]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=102&search=Self-Destruct|Spell Link]]

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