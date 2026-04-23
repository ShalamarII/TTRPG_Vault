---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Bottle
spellCollege: [Food]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent."'
spellCastingTime: '""'
spellCost: "1 quart of food to be prepared. For 2 points extra"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Portion, Cook. Shape Earth and Shape Metal is required if the mage wishes to create]
spellPrereqText: Portion, Cook. Shape Earth and Shape Metal is required if the mage wishes to create
spellSource: Codex Arcanum
spellReference: GOCA109
spellLink: [[Codex Arcanum.pdf#page=109&search=Bottle]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=109&search=Bottle|Spell Link]]

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