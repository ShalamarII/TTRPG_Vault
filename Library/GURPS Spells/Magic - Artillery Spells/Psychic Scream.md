---
tags:
  - Spell
  - SpellsAsMagic
spellID: pCQsreu4yaRUS6jGg 
spellName: Psychic Scream
spellCollege: [Communication & Empathy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 secs"'
spellCastingTime: '"1 sec/yard radius"'
spellCost: "3/yard radius"
spellMaintenance: "undefined"
spellPrerequisites: [Mind-Sending, Magery4, 10 Spell(s) from the Communications & Empathy College, ]
spellPrereqText: Mind-Sending, Magery4, 10 Spell(s) from the Communications & Empathy College
spellSource: Magic - Artillery Spells
spellReference: MAS12
spellLink: [[Magic - Artillery Spells.pdf#page=12&search=Psychic Scream]]
spellPoints: 1
spellTags: Artillery, Communication & Empathy
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=12&search=Psychic Scream|Spell Link]]

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