---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Summon Minor Elemental
spellCollege: [Elemental Spirit and Common Elemental Spells]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"1 hour, can't be maintained."'
spellCastingTime: '"1 second per energy point."'
spellCost: "2"
spellMaintenance: "same to maintain"
spellPrerequisites: [4 other spells of the appropriate element]
spellPrereqText: 4 other spells of the appropriate element
spellSource: Codex Arcanum
spellReference: GOCA157
spellLink: [[Codex Arcanum.pdf#page=157&search=Summon Minor Elemental]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=157&search=Summon Minor Elemental|Spell Link]]

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