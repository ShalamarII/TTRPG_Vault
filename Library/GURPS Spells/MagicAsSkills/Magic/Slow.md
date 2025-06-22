---
tags:
  - Spell
  - SpellsAsMagic
spellID: pLp_AoWf7Ue6iA3V6 
spellName: Slow
spellCollege: [Movement]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"10 sec"'
spellCastingTime: '"3 sec"'
spellCost: "5"
spellMaintenance: "4"
spellPrerequisites: [Magery 1, Movement 1, Haste, Hinder, ]
spellPrereqText: Magery 1, Movement 1, Haste, Hinder
spellSource: Magic
spellReference: M145
spellLink: [[Magic.pdf#page=147&search=Slow]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic.pdf#page=147&search=Slow|Spell Link]]

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