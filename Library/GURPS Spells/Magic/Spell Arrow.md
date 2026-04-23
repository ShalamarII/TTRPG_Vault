---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBvrkWHt5BQdktKsf 
spellName: Spell Arrow
spellCollege: [Enchantment]
spellDifficulty: IQ/H
spellClass: Enchantment
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"-"'
spellCost: "30xspell cost"
spellMaintenance: "-"
spellPrerequisites: [Spell Stone, ]
spellPrereqText: Spell Stone
spellSource: Magic
spellReference: M65
spellLink: [[Magic.pdf#page=67&search=Spell Arrow]]
spellPoints: 1
spellTags: Weapon Enchantment
spellWeapons: 
---

 [[Magic.pdf#page=67&search=Spell Arrow|Spell Link]]

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