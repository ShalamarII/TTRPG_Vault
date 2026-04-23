---
tags:
  - Spell
  - SpellsAsMagic
spellID: pMvXaSaa9paZp3QMC 
spellName: Rain of Nuts
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1 per 10 yds"
spellMaintenance: "Same"
spellPrerequisites: [Shape Plant, 5 Spell(s) from the Plant College, Magery 1, Plant 1, ]
spellPrereqText: Shape Plant, 5 Spell(s) from the Plant College, Magery 1, Plant 1
spellSource: Magic
spellReference: M165
spellLink: [[Magic.pdf#page=167&search=Rain of Nuts]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic.pdf#page=167&search=Rain of Nuts|Spell Link]]

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