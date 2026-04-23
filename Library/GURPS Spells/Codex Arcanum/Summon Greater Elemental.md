---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Summon Greater Elemental
spellCollege: [Elemental Spirit and Common Elemental Spells]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"1 hour. May not be maintained"'
spellCastingTime: '"1 minute"'
spellCost: "12"
spellMaintenance: "same to maintain"
spellPrerequisites: [Summon Elemental, 12 spells of the appropriate element or Summon Greater]
spellPrereqText: Summon Elemental, 12 spells of the appropriate element or Summon Greater
spellSource: Codex Arcanum
spellReference: GOCA157
spellLink: [[Codex Arcanum.pdf#page=157&search=Summon Greater Elemental]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=157&search=Summon Greater Elemental|Spell Link]]

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