---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBqVkd0RGf3YQQvoT 
spellName: Recall
spellCollege: [Knowledge, Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 day"'
spellCastingTime: '"10 sec"'
spellCost: "4"
spellMaintenance: "-"
spellPrerequisites: [History, Memorize, Magery 2, Knowledge 2, Mind Control 2, ]
spellPrereqText: History, Memorize, Magery 2, Knowledge 2, Mind Control 2
spellSource: Magic
spellReference: M106
spellLink: [[Magic.pdf#page=108&search=Recall]]
spellPoints: 1
spellTags: Knowledge, Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=108&search=Recall|Spell Link]]

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