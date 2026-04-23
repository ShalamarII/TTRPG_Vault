---
tags:
  - Spell
  - SpellsAsMagic
spellID: pnD3Eo1buHeDDv5t2 
spellName: Resist Lightning
spellCollege: [Air, Protection & Warning, Weather]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [6 Spell(s) from the Air College, ]
spellPrereqText: 6 Spell(s) from the Air College
spellSource: Magic
spellReference: M196
spellLink: [[Magic.pdf#page=198&search=Resist Lightning]]
spellPoints: 1
spellTags: Air, Protection & Warning, Weather
spellWeapons: 
---

 [[Magic.pdf#page=198&search=Resist Lightning|Spell Link]]

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