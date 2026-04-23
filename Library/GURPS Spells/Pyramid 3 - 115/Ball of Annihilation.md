---
tags:
  - Spell
  - SpellsAsMagic
spellID: pT1FHk9cZ4mSZ0EuX 
spellName: Ball of Annihilation
spellCollege: [Gate, Movement]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"4 sec"'
spellCost: "20"
spellMaintenance: "10"
spellPrerequisites: [Pull, Planar Summons, Drain Mana, ]
spellPrereqText: Pull, Planar Summons, Drain Mana
spellSource: Pyramid 3 - 115
spellReference: PY115:20
spellLink: [[Pyramid 3 - 115.pdf#page=20&search=Ball of Annihilation]]
spellPoints: 1
spellTags: Gate, Movement
spellWeapons: 
---

 [[Pyramid 3 - 115.pdf#page=20&search=Ball of Annihilation|Spell Link]]

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