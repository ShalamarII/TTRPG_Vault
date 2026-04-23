---
tags:
  - Spell
  - SpellsAsMagic
spellID: pdcC_utWqD6fmAGEP 
spellName: Alertness
spellCollege: [Mind Control]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 min"'
spellCastingTime: '"1 sec"'
spellCost: "2/pt increase"
spellMaintenance: "Half"
spellPrerequisites: [Keen, ]
spellPrereqText: Keen
spellSource: Magic
spellReference: M133
spellLink: [[Magic.pdf#page=135&search=Alertness]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=135&search=Alertness|Spell Link]]

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