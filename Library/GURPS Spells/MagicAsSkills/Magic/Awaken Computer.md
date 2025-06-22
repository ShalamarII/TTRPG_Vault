---
tags:
  - Spell
  - SpellsAsMagic
spellID: pIS6UQvkJIoT9I2Pz 
spellName: Awaken Computer
spellCollege: [Technological]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "8"
spellMaintenance: "2"
spellPrerequisites: [Animation, Wisdom, ]
spellPrereqText: Animation, Wisdom
spellSource: Magic
spellReference: M178
spellLink: [[Magic.pdf#page=180&search=Awaken Computer]]
spellPoints: 1
spellTags: Machine, Technological
spellWeapons: 
---

 [[Magic.pdf#page=180&search=Awaken Computer|Spell Link]]

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