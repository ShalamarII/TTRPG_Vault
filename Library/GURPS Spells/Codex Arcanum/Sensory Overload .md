---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Sensory Overload 
spellCollege: [Mind Control]
spellDifficulty: 
spellClass: 
spellResisted: IQ
spellDuration: '"30 Seconds."'
spellCastingTime: '"10 Seconds."'
spellCost: "4 to cast"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Magery 2, Alertness, 5 Body Control Spells]
spellPrereqText: Magery 2, Alertness, 5 Body Control Spells
spellSource: Codex Arcanum
spellReference: GOCA402
spellLink: [[Codex Arcanum.pdf#page=402&search=Sensory Overload ]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=402&search=Sensory Overload |Spell Link]]

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