---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Transmute to Iron
spellCollege: [Earth]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '"1 minute"'
spellCost: "3 per 50 lbs. of material"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Magery 2, Create Metal, Earth to Metal, 5 other Metal spells.]
spellPrereqText: Magery 2, Create Metal, Earth to Metal, 5 other Metal spells.
spellSource: Codex Arcanum
spellReference: GOCA196
spellLink: [[Codex Arcanum.pdf#page=196&search=Transmute to Iron]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=196&search=Transmute to Iron|Spell Link]]

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