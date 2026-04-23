---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Extended Range
spellCollege: [Meta]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 seconds or until the other spell is cast, whichever is less."'
spellCastingTime: '"3 seconds per doubling of normal range."'
spellCost: "1 per each doubling of normal range"
spellMaintenance: "same to maintain"
spellPrerequisites: [Magery, 5 Metaspells]
spellPrereqText: Magery, 5 Metaspells
spellSource: Codex Arcanum
spellReference: GOCA352
spellLink: [[Codex Arcanum.pdf#page=352&search=Extended Range]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=352&search=Extended Range|Spell Link]]

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