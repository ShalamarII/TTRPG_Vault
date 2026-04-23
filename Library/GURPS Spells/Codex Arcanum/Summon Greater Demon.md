---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Summon Greater Demon
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"Until Instability sets in . . ."'
spellCastingTime: '"5 minutes"'
spellCost: "20"
spellMaintenance: ""
spellPrerequisites: [Magery and at least the Chaos Mark of the Chaos God in question.]
spellPrereqText: Magery and at least the Chaos Mark of the Chaos God in question.
spellSource: Codex Arcanum
spellReference: GOCA455
spellLink: [[Codex Arcanum.pdf#page=455&search=Summon Greater Demon]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=455&search=Summon Greater Demon|Spell Link]]

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