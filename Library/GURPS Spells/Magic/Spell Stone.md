---
tags:
  - Spell
  - SpellsAsMagic
spellID: pdPnMC0Usqr6ulUZ5 
spellName: Spell Stone
spellCollege: [Enchantment]
spellDifficulty: IQ/H
spellClass: Enchantment
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"-"'
spellCost: "20xspell cost"
spellMaintenance: "-"
spellPrerequisites: [Delay, Enchant, ]
spellPrereqText: Delay, Enchant
spellSource: Magic
spellReference: M60
spellLink: [[Magic.pdf#page=62&search=Spell Stone]]
spellPoints: 1
spellTags: Enchantment
spellWeapons: 
---

 [[Magic.pdf#page=62&search=Spell Stone|Spell Link]]

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