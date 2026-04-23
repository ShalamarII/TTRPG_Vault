---
tags:
  - Spell
  - SpellsAsMagic
spellID: ps_MPr56X07P9EIXr 
spellName: Sorcerer's Stand-In
spellCollege: [Enchantment]
spellDifficulty: IQ/A
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 day"'
spellCastingTime: '"1 min"'
spellCost: "8"
spellMaintenance: "-"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS9
spellLink: [[Magic - The Least of Spells.pdf#page=9&search=Sorcerer's Stand-In]]
spellPoints: 1
spellTags: Enchantment
spellWeapons: 
---

 [[Magic - The Least of Spells.pdf#page=9&search=Sorcerer's Stand-In|Spell Link]]

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