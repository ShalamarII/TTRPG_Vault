---
tags:
  - Spell
  - SpellsAsMagic
spellID: pHWjs1xt2NB9mXsBj 
spellName: Cool
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"1 min"'
spellCost: "1/10"
spellMaintenance: "Same"
spellPrerequisites: [4 Spell(s) from the Air College, Cold, ]
spellPrereqText: 4 Spell(s) from the Air College, Cold
spellSource: Magic
spellReference: M195
spellLink: [[Magic.pdf#page=197&search=Cool]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: 
---

 [[Magic.pdf#page=197&search=Cool|Spell Link]]

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