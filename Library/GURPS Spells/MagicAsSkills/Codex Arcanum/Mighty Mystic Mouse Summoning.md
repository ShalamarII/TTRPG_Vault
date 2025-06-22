---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Mighty Mystic Mouse Summoning
spellCollege: [Animal]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"2 minutes"'
spellCastingTime: '"30 seconds"'
spellCost: "8"
spellMaintenance: "4 to maintain"
spellPrerequisites: [Magery, Rider Within and 5 other animal spells, 2 metaspells, and Summon Spirit.]
spellPrereqText: Magery, Rider Within and 5 other animal spells, 2 metaspells, and Summon Spirit.
spellSource: Codex Arcanum
spellReference: GOCA26
spellLink: [[Codex Arcanum.pdf#page=26&search=Mighty Mystic Mouse Summoning]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=26&search=Mighty Mystic Mouse Summoning|Spell Link]]

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