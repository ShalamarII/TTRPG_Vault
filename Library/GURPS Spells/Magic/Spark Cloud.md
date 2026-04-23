---
tags:
  - Spell
  - SpellsAsMagic
spellID: pJ6azRlYimXjgH-k3 
spellName: Spark Cloud
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"10 sec"'
spellCastingTime: '"1-5 sec"'
spellCost: "1-5"
spellMaintenance: "-"
spellPrerequisites: [Lightning, Shape Air, ]
spellPrereqText: Lightning, Shape Air
spellSource: Magic
spellReference: M196
spellLink: [[Magic.pdf#page=198&search=Spark Cloud]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"w3xAvhJw6NhptZDXc","damage":{"type":"point burn/second","base":"1"},"usage":"Area","calc":{"damage":"1 point burn/second"}}]
---

 [[Magic.pdf#page=198&search=Spark Cloud|Spell Link]]

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