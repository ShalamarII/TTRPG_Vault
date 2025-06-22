---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Summon Undead
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"1 hour (creatures commanded to service stay until the spell ends, their task is complete,"'
spellCastingTime: '"1 minute"'
spellCost: "6"
spellMaintenance: "3 to maintain"
spellPrerequisites: [Summon Spirit]
spellPrereqText: Summon Spirit
spellSource: Codex Arcanum
spellReference: GOCA449
spellLink: [[Codex Arcanum.pdf#page=449&search=Summon Undead]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=449&search=Summon Undead|Spell Link]]

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