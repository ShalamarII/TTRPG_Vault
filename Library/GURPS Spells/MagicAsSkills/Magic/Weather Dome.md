---
tags:
  - Spell
  - SpellsAsMagic
spellID: pArejST639oGWHLGo 
spellName: Weather Dome
spellCollege: [Protection & Warning, Weather]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"6 hrs"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "2"
spellPrerequisites: [2 Spell(s) from the Water College, 2 Spell(s) from the Earth College, 2 Spell(s) from the Fire College, 2 Spell(s) from the Air College, ]
spellPrereqText: 2 Spell(s) from the Water College, 2 Spell(s) from the Earth College, 2 Spell(s) from the Fire College, 2 Spell(s) from the Air College
spellSource: Magic
spellReference: M169
spellLink: [[Magic.pdf#page=171&search=Weather Dome]]
spellPoints: 1
spellTags: Protection & Warning, Weather
spellWeapons: 
---

 [[Magic.pdf#page=171&search=Weather Dome|Spell Link]]

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