---
tags:
  - Spell
  - SpellsAsMagic
spellID: pzlrJh9DgJOLzbTMQ 
spellName: Redline
spellCollege: [Movement, Technological]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 day"'
spellCastingTime: '"1 min"'
spellCost: "4"
spellMaintenance: "-"
spellPrerequisites: [Quick March, ]
spellPrereqText: Quick March
spellSource: Pyramid 3 - 115
spellReference: PY115:14
spellLink: [[Pyramid 3 - 115.pdf#page=14&search=Redline]]
spellPoints: 1
spellTags: Machine, Movement, Technological
spellWeapons: 
---

 [[Pyramid 3 - 115.pdf#page=14&search=Redline|Spell Link]]

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