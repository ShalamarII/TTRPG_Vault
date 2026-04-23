---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBFgBoHLix9DoeiVJ 
spellName: Nightingale
spellCollege: [Protection & Warning]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"10 hrs"'
spellCastingTime: '"1 sec"'
spellCost: "2"
spellMaintenance: "Same"
spellPrerequisites: [Sense Danger, ]
spellPrereqText: Sense Danger
spellSource: Magic
spellReference: M167
spellLink: [[Magic.pdf#page=169&search=Nightingale]]
spellPoints: 1
spellTags: Protection & Warning
spellWeapons: 
---

 [[Magic.pdf#page=169&search=Nightingale|Spell Link]]

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