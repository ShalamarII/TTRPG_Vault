---
tags:
  - Spell
  - SpellsAsMagic
spellID: pQwYsrDCosqnnQZY5 
spellName: Counterspell
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Subject spell
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "Half countered spell"
spellMaintenance: "undefined"
spellPrerequisites: [Magery 1, Meta 1, ]
spellPrereqText: Magery 1, Meta 1
spellSource: Magic
spellReference: M121
spellLink: [[Magic.pdf#page=123&search=Counterspell]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=123&search=Counterspell|Spell Link]]

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