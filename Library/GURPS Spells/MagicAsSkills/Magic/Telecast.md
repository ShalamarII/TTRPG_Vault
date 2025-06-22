---
tags:
  - Spell
  - SpellsAsMagic
spellID: pQGixzhQ8buZNJln- 
spellName: Telecast
spellCollege: [Meta]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: undefined
spellDuration: '"5 sec"'
spellCastingTime: '"1 min"'
spellCost: "same as Teleport"
spellMaintenance: "Same"
spellPrerequisites: [1 Spell(s) from 10 Colleges, Teleport, Wizard Eye, Magery 3, Meta 3, ]
spellPrereqText: 1 Spell(s) from 10 Colleges, Teleport, Wizard Eye, Magery 3, Meta 3
spellSource: Magic
spellReference: M128
spellLink: [[Magic.pdf#page=130&search=Telecast]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=130&search=Telecast|Spell Link]]

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