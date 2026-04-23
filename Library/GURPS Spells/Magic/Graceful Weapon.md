---
tags:
  - Spell
  - SpellsAsMagic
spellID: p9tgqzxKo3_X0V3uy 
spellName: Graceful Weapon
spellCollege: [Enchantment]
spellDifficulty: IQ/H
spellClass: Enchantment
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"-"'
spellCost: "150/lb"
spellMaintenance: "-"
spellPrerequisites: [Apportation, Enchant, ]
spellPrereqText: Apportation, Enchant
spellSource: Magic
spellReference: M63
spellLink: [[Magic.pdf#page=65&search=Graceful Weapon]]
spellPoints: 1
spellTags: Weapon Enchantment
spellWeapons: 
---

 [[Magic.pdf#page=65&search=Graceful Weapon|Spell Link]]

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