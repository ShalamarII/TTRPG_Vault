---
tags:
  - Spell
  - SpellsAsMagic
spellID: p33MWY6Ok-rLvoP5l 
spellName: Cloud of Doom
spellCollege: [Air]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"5 secs"'
spellCastingTime: '"1 sec"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Stench, Devitalize Air, Magery4, 10 Spell(s) from the Air College, ]
spellPrereqText: Stench, Devitalize Air, Magery4, 10 Spell(s) from the Air College
spellSource: Magic - Artillery Spells
spellReference: MAS9
spellLink: [[Magic - Artillery Spells.pdf#page=9&search=Cloud of Doom]]
spellPoints: 1
spellTags: Air, Artillery
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=9&search=Cloud of Doom|Spell Link]]

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