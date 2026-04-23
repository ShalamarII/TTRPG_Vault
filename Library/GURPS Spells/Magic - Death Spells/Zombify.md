---
tags:
  - Spell
  - SpellsAsMagic
spellID: ppTt-ypImuTA2cwmV 
spellName: Zombify
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: -
spellDuration: '"Subject's HT-10 min, permanent afterwards"'
spellCastingTime: '"1 min"'
spellCost: "10"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Necromancy 3, Pestilence, Zombie, ]
spellPrereqText: Magery 3, Necromancy 3, Pestilence, Zombie
spellSource: Magic - Death Spells
spellReference: MDS18
spellLink: [[Magic - Death Spells.pdf#page=18&search=Zombify]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=18&search=Zombify|Spell Link]]

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