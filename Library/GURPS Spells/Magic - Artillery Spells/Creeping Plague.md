---
tags:
  - Spell
  - SpellsAsMagic
spellID: pKtbsXNYVOtrbeZsg 
spellName: Creeping Plague
spellCollege: [Animal]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"1 minute"'
spellCastingTime: '"2 secs"'
spellCost: "2"
spellMaintenance: "Same"
spellPrerequisites: [Magery5, Beast-Summoning, Magery4, Create Animal, ]
spellPrereqText: Magery5, Beast-Summoning, Magery4, Create Animal
spellSource: Magic - Artillery Spells
spellReference: MAS10
spellLink: [[Magic - Artillery Spells.pdf#page=10&search=Creeping Plague]]
spellPoints: 1
spellTags: Animal, Artillery
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=10&search=Creeping Plague|Spell Link]]

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