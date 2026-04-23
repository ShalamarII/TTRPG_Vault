---
tags:
  - Spell
  - SpellsAsMagic
spellID: p7B4nrWcPG4j52zBH 
spellName: Plant Sense
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Hide Path
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "2"
spellPrerequisites: [Forest Warning, Hide Path, ]
spellPrereqText: Forest Warning, Hide Path
spellSource: Magic
spellReference: M163
spellLink: [[Magic.pdf#page=165&search=Plant Sense]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic.pdf#page=165&search=Plant Sense|Spell Link]]

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