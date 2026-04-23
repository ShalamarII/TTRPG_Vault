---
tags:
  - Spell
  - SpellsAsMagic
spellID: p0MJ8TlQri9YGdVW5 
spellName: Sleep
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Until awakened"'
spellCastingTime: '"3 sec"'
spellCost: "4"
spellMaintenance: "-"
spellPrerequisites: [Daze, ]
spellPrereqText: Daze
spellSource: Magic
spellReference: M135
spellLink: [[Magic.pdf#page=137&search=Sleep]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=137&search=Sleep|Spell Link]]

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