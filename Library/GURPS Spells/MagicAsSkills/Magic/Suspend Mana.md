---
tags:
  - Spell
  - SpellsAsMagic
spellID: p93k59FROfBdtBd5C 
spellName: Suspend Mana
spellCollege: [Meta]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"10 min"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [1 Spell(s) from 10 Colleges, Suspend Magic, ]
spellPrereqText: 1 Spell(s) from 10 Colleges, Suspend Magic
spellSource: Magic
spellReference: M125
spellLink: [[Magic.pdf#page=127&search=Suspend Mana]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=127&search=Suspend Mana|Spell Link]]

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