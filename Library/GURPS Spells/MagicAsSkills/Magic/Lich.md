---
tags:
  - Spell
  - SpellsAsMagic
spellID: pweNB9OIQQNzJIqeH 
spellName: Lich
spellCollege: [Enchantment, Necromancy]
spellDifficulty: IQ/VH
spellClass: Enchantment
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"Varies"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Enchant, Soul Jar, Zombie, Magery 3, Enchantment 3, Necromancy 3, at least 13 IQ, ]
spellPrereqText: Enchant, Soul Jar, Zombie, Magery 3, Enchantment 3, Necromancy 3, at least 13 IQ
spellSource: Magic
spellReference: M159
spellLink: [[Magic.pdf#page=161&search=Lich]]
spellPoints: 1
spellTags: Enchantment, Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=161&search=Lich|Spell Link]]

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