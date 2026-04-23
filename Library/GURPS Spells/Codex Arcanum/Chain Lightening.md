---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Chain Lightening
spellCollege: [Electricity]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 second per die of damage."'
spellCost: "2 per die of damage"
spellMaintenance: "half to maintain"
spellPrerequisites: [Magery, Lightening]
spellPrereqText: Magery, Lightening
spellSource: Codex Arcanum
spellReference: GOCA5
spellLink: [[Codex Arcanum.pdf#page=5&search=Chain Lightening]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=5&search=Chain Lightening|Spell Link]]

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