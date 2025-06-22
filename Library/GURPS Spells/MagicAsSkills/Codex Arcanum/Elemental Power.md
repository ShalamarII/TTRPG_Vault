---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Elemental Power
spellCollege: [Elemental Spirit and Common Elemental Spells]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"1 minute"'
spellCastingTime: '"5 seconds"'
spellCost: "None to Cast:; 1 to maintain. This maintenance cost is not reduced by high skill."
spellMaintenance: "same to maintain"
spellPrerequisites: [Magery, 10 Elemental College spells from the appropriate college.]
spellPrereqText: Magery, 10 Elemental College spells from the appropriate college.
spellSource: Codex Arcanum
spellReference: GOCA156
spellLink: [[Codex Arcanum.pdf#page=156&search=Elemental Power]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=156&search=Elemental Power|Spell Link]]

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