---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVnHzs7Fj3yoo2mV1 
spellName: Final Rest
spellCollege: [Healing, Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"10 min"'
spellCost: "20"
spellMaintenance: "-"
spellPrerequisites: [Spirit Empathy, Magery 1, Healing 1, ]
spellPrereqText: Spirit Empathy, Magery 1, Healing 1
spellSource: Magic
spellReference: M89
spellLink: [[Magic.pdf#page=91&search=Final Rest]]
spellPoints: 1
spellTags: Healing, Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=91&search=Final Rest|Spell Link]]

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