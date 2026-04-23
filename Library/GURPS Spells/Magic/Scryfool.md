---
tags:
  - Spell
  - SpellsAsMagic
spellID: pxwTIlb9c0iRhGrH2 
spellName: Scryfool
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Special
spellDuration: '"10 hrs"'
spellCastingTime: '"10 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Sense Observation, Simple Illusion, Magery 2, Meta 2, ]
spellPrereqText: Sense Observation, Simple Illusion, Magery 2, Meta 2
spellSource: Magic
spellReference: M123
spellLink: [[Magic.pdf#page=125&search=Scryfool]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=125&search=Scryfool|Spell Link]]

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