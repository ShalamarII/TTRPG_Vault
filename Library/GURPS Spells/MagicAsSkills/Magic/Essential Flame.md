---
tags:
  - Spell
  - SpellsAsMagic
spellID: puezLkN9XlGcMG4eq 
spellName: Essential Flame
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"3 sec"'
spellCost: "3#"
spellMaintenance: "2"
spellPrerequisites: [6 Spell(s) from the Fire College, ]
spellPrereqText: 6 Spell(s) from the Fire College
spellSource: Magic
spellReference: M75
spellLink: [[Magic.pdf#page=77&search=Essential Flame]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"wUeCyLb86qFDDwlQV","damage":{"type":"burn","base":"1d"},"usage":"Area","calc":{"damage":"1d burn"}}]
---

 [[Magic.pdf#page=77&search=Essential Flame|Spell Link]]

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