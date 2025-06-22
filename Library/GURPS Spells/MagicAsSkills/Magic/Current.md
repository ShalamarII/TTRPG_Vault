---
tags:
  - Spell
  - SpellsAsMagic
spellID: pF8xYlxOfmQAWEctM 
spellName: Current
spellCollege: [Water, Weather]
spellDifficulty: IQ/H
spellClass: Special/Area
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"1 min"'
spellCost: "1/50"
spellMaintenance: "Same"
spellPrerequisites: [6 Spell(s) from the Water College, ]
spellPrereqText: 6 Spell(s) from the Water College
spellSource: Magic
spellReference: M194
spellLink: [[Magic.pdf#page=196&search=Current]]
spellPoints: 1
spellTags: Water, Weather
spellWeapons: 
---

 [[Magic.pdf#page=196&search=Current|Spell Link]]

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