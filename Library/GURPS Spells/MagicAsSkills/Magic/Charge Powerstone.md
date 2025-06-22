---
tags:
  - Spell
  - SpellsAsMagic
spellID: p_xmqkL-zVgu_y9xS 
spellName: Charge Powerstone
spellCollege: [Meta]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"until used"'
spellCastingTime: '"10 min"'
spellCost: "3/pt of energy"
spellMaintenance: "-"
spellPrerequisites: [Powerstone, Lend Energy, Magery 3, Meta 3, ]
spellPrereqText: Powerstone, Lend Energy, Magery 3, Meta 3
spellSource: Magic
spellReference: M126
spellLink: [[Magic.pdf#page=128&search=Charge Powerstone]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=128&search=Charge Powerstone|Spell Link]]

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