---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Water of Life
spellCollege: [Healing]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 hour"'
spellCastingTime: '"1 minute"'
spellCost: "1 point per quart of water (4 per gallon)"
spellMaintenance: "3 to maintain"
spellPrerequisites: [Major, Minor Healing, Sterilize, Purify Water]
spellPrereqText: Major, Minor Healing, Sterilize, Purify Water
spellSource: Codex Arcanum
spellReference: GOCA252
spellLink: [[Codex Arcanum.pdf#page=252&search=Water of Life]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=252&search=Water of Life|Spell Link]]

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