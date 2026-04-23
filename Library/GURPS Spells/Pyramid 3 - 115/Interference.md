---
tags:
  - Spell
  - SpellsAsMagic
spellID: p3cb6-1Tc9xg82IQF 
spellName: Interference
spellCollege: [Technological]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [Jam Radio, ]
spellPrereqText: Jam Radio
spellSource: Pyramid 3 - 115
spellReference: PY115:14
spellLink: [[Pyramid 3 - 115.pdf#page=14&search=Interference]]
spellPoints: 1
spellTags: Energy, Technological
spellWeapons: 
---

 [[Pyramid 3 - 115.pdf#page=14&search=Interference|Spell Link]]

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