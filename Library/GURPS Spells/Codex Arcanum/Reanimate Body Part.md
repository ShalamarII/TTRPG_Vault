---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Reanimate Body Part
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 minute"'
spellCastingTime: '"3 seconds"'
spellCost: "2 for a hand or head"
spellMaintenance: "3 for an arm or leg, same to maintain"
spellPrerequisites: [Zombie]
spellPrereqText: Zombie
spellSource: Codex Arcanum
spellReference: GOCA442
spellLink: [[Codex Arcanum.pdf#page=442&search=Reanimate Body Part]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=442&search=Reanimate Body Part|Spell Link]]

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