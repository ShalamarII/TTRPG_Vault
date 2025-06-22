---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Quintessence
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Enchantment
spellResisted: 
spellDuration: '""'
spellCastingTime: '"1 minute"'
spellCost: "25 points per 'dose' for common quintessences"
spellMaintenance: ""
spellPrerequisites: [Magery 2, 10 Mind Control and/or Communication and Empathy Spells, Alchemy 13+]
spellPrereqText: Magery 2, 10 Mind Control and/or Communication and Empathy Spells, Alchemy 13+
spellSource: Codex Arcanum
spellReference: GOCA93
spellLink: [[Codex Arcanum.pdf#page=93&search=Quintessence]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=93&search=Quintessence|Spell Link]]

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