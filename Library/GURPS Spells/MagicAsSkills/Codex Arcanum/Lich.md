---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Lich
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Enchantment
spellResisted: 
spellDuration: '"1 hour"'
spellCastingTime: '"10 seconds"'
spellCost: "10"
spellMaintenance: "3 to maintain"
spellPrerequisites: [Magery 2, Soul Jar, Zombie, 6 Other Necromantic Spells, 20 spells from 10 different]
spellPrereqText: Magery 2, Soul Jar, Zombie, 6 Other Necromantic Spells, 20 spells from 10 different
spellSource: Codex Arcanum
spellReference: GOCA433
spellLink: [[Codex Arcanum.pdf#page=433&search=Lich]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=433&search=Lich|Spell Link]]

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