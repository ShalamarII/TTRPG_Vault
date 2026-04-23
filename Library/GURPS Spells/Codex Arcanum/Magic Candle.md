---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Magic Candle
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Enchantment
spellResisted: 
spellDuration: '"Variable. (a candle lasts 1d6 minutes per 'charge' put into it.)"'
spellCastingTime: '"1 minute"'
spellCost: "1 point per 'charge' given to the candle. The type of 'charge' must be specified before"
spellMaintenance: ""
spellPrerequisites: [Divination (Crystal-gazing) Mana Collector Enchantment]
spellPrereqText: Divination (Crystal-gazing) Mana Collector Enchantment
spellSource: Codex Arcanum
spellReference: GOCA105
spellLink: [[Codex Arcanum.pdf#page=105&search=Magic Candle]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=105&search=Magic Candle|Spell Link]]

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