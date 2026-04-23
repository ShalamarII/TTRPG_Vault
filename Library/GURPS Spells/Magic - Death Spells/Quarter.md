---
tags:
  - Spell
  - SpellsAsMagic
spellID: pUiY7UboS82uuv2b1 
spellName: Quarter
spellCollege: [Movement]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "15"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Movement 3, 10 Spell(s) from the Movement College, Pull, Repel, ]
spellPrereqText: Magery 3, Movement 3, 10 Spell(s) from the Movement College, Pull, Repel
spellSource: Magic - Death Spells
spellReference: MDS18
spellLink: [[Magic - Death Spells.pdf#page=18&search=Quarter]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=18&search=Quarter|Spell Link]]

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