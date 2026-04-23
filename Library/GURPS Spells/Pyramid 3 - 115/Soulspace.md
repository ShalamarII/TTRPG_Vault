---
tags:
  - Spell
  - SpellsAsMagic
spellID: pGPF8gP-e1yJiHerT 
spellName: Soulspace
spellCollege: [Enchantment]
spellDifficulty: IQ/H
spellClass: Enchantment
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"-"'
spellCost: "5000 +1/10 users"
spellMaintenance: "-"
spellPrerequisites: [Machine Speech, Enchant, Communication, ]
spellPrereqText: Machine Speech, Enchant, Communication
spellSource: Pyramid 3 - 115
spellReference: PY115:22
spellLink: [[Pyramid 3 - 115.pdf#page=22&search=Soulspace]]
spellPoints: 1
spellTags: Enchantment
spellWeapons: 
---

 [[Pyramid 3 - 115.pdf#page=22&search=Soulspace|Spell Link]]

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