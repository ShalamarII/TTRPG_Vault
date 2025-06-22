---
tags:
  - Spell
  - SpellsAsMagic
spellID: pSRM2wVeZMLnYPrY_ 
spellName: Simulacrum
spellCollege: [Enchantment]
spellDifficulty: IQ/VH
spellClass: Enchantment
spellResisted: undefined
spellDuration: '"Permanent#"'
spellCastingTime: '"-"'
spellCost: "2xgolem"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Enchantment 3, Golem, Perfect Illusion, Illusion Disguise, ]
spellPrereqText: Magery 3, Enchantment 3, Golem, Perfect Illusion, Illusion Disguise
spellSource: Magic
spellReference: M61
spellLink: [[Magic.pdf#page=63&search=Simulacrum]]
spellPoints: 1
spellTags: Enchantment
spellWeapons: 
---

 [[Magic.pdf#page=63&search=Simulacrum|Spell Link]]

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