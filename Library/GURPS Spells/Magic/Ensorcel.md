---
tags:
  - Spell
  - SpellsAsMagic
spellID: pEcQp_be5dBf3nSTi 
spellName: Ensorcel
spellCollege: [Enchantment]
spellDifficulty: IQ/VH
spellClass: Enchantment
spellResisted: Special
spellDuration: '"Permanent"'
spellCastingTime: '"-"'
spellCost: "200xspell cost"
spellMaintenance: "-"
spellPrerequisites: [Malefice, ]
spellPrereqText: Malefice
spellSource: Magic
spellReference: M60
spellLink: [[Magic.pdf#page=62&search=Ensorcel]]
spellPoints: 1
spellTags: Enchantment
spellWeapons: 
---

 [[Magic.pdf#page=62&search=Ensorcel|Spell Link]]

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