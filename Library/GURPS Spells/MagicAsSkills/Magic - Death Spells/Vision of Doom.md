---
tags:
  - Spell
  - SpellsAsMagic
spellID: p8ez5TYf88CEiwk1i 
spellName: Vision of Doom
spellCollege: [Knowledge]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: IQ
spellDuration: '"Lasting, until subject dies, fails at suicide and resists, or is saved by Remove Curse"'
spellCastingTime: '"3 sec"'
spellCost: "10"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Knowledge 3, Summon Shade, ]
spellPrereqText: Magery 3, Knowledge 3, Summon Shade
spellSource: Magic - Death Spells
spellReference: MDS15
spellLink: [[Magic - Death Spells.pdf#page=15&search=Vision of Doom]]
spellPoints: 1
spellTags: Knowledge
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=15&search=Vision of Doom|Spell Link]]

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