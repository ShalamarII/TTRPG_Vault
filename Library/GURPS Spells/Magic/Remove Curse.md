---
tags:
  - Spell
  - SpellsAsMagic
spellID: p6PW7gfNJ0ruci9ej 
spellName: Remove Curse
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Subject spell
spellDuration: '"Permanent"'
spellCastingTime: '"1 hr"'
spellCost: "20"
spellMaintenance: "-"
spellPrerequisites: [1 Spell(s) from 15 Colleges, Magery 2, Meta 2, ]
spellPrereqText: 1 Spell(s) from 15 Colleges, Magery 2, Meta 2
spellSource: Magic
spellReference: M126
spellLink: [[Magic.pdf#page=128&search=Remove Curse]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=128&search=Remove Curse|Spell Link]]

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