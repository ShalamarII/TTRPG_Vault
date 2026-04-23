---
tags:
  - Spell
  - SpellsAsMagic
spellID: p5q9e6dnMQ3iBrz58 
spellName: Walk Through Water
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"3 sec"'
spellCost: "4"
spellMaintenance: "3"
spellPrerequisites: [Magery 1, Water 1, Shape Water, ]
spellPrereqText: Magery 1, Water 1, Shape Water
spellSource: Magic
spellReference: M188
spellLink: [[Magic.pdf#page=190&search=Walk Through Water]]
spellPoints: 1
spellTags: Water
spellWeapons: 
---

 [[Magic.pdf#page=190&search=Walk Through Water|Spell Link]]

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