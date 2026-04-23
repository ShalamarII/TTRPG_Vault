---
tags:
  - Spell
  - SpellsAsMagic
spellID: pc0J8tXGP7WaZ5M2D 
spellName: Perilous Pulsations
spellCollege: [Sound]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"5 secs"'
spellCastingTime: '"3 secs"'
spellCost: "5"
spellMaintenance: "Same"
spellPrerequisites: [Concussion, Sound Jet, 7 Spell(s) from the Sound College, Magery4, ]
spellPrereqText: Concussion, Sound Jet, 7 Spell(s) from the Sound College, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS25
spellLink: [[Magic - Artillery Spells.pdf#page=25&search=Perilous Pulsations]]
spellPoints: 1
spellTags: Artillery, Sound
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=25&search=Perilous Pulsations|Spell Link]]

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