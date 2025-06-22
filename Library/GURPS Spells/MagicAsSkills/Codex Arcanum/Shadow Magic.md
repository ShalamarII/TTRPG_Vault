---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Shadow Magic
spellCollege: [Illusion and Creation]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"1 minute or the Duration of the spell being mimicked, whichever is less."'
spellCastingTime: '"5 seconds"'
spellCost: "5 to cast"
spellMaintenance: "half that to maintain"
spellPrerequisites: [Perfect Illusion]
spellPrereqText: Perfect Illusion
spellSource: Codex Arcanum
spellReference: GOCA272
spellLink: [[Codex Arcanum.pdf#page=272&search=Shadow Magic]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=272&search=Shadow Magic|Spell Link]]

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