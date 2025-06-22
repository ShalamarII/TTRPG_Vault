---
tags:
  - Spell
  - SpellsAsMagic
spellID: pD2NVaNgJTit9XKcb 
spellName: Air Vortex
spellCollege: [Air, Movement, Fire]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: HT or DX
spellDuration: '"10 sec"'
spellCastingTime: '"2 sec"'
spellCost: "8"
spellMaintenance: "3"
spellPrerequisites: [Magery 2, Air 2, Movement 2, Windstorm, Body Of Air, ]
spellPrereqText: Magery 2, Air 2, Movement 2, Windstorm, Body Of Air
spellSource: Magic
spellReference: M26
spellLink: [[Magic.pdf#page=28&search=Air Vortex]]
spellPoints: 1
spellTags: Air, Movement
spellWeapons: 
---

 [[Magic.pdf#page=28&search=Air Vortex|Spell Link]]

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