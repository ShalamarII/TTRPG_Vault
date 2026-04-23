---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Vampiric Regeneration
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 seconds or one successful strike, whichever comes first."'
spellCastingTime: '"3 seconds"'
spellCost: "4"
spellMaintenance: "3 to maintain"
spellPrerequisites: [Magery, Steal Health, Puissance]
spellPrereqText: Magery, Steal Health, Puissance
spellSource: Codex Arcanum
spellReference: GOCA452
spellLink: [[Codex Arcanum.pdf#page=452&search=Vampiric Regeneration]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=452&search=Vampiric Regeneration|Spell Link]]

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