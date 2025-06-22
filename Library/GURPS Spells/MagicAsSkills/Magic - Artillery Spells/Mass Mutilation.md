---
tags:
  - Spell
  - SpellsAsMagic
spellID: pAu4VsdK1MI8M0f39 
spellName: Mass Mutilation
spellCollege: [Mind Control]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: Will
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec/yard"'
spellCost: "4"
spellMaintenance: "undefined"
spellPrerequisites: [Madness, Mass Suggestion, 10 Spell(s) from the Mind Control College, Magery4, ]
spellPrereqText: Madness, Mass Suggestion, 10 Spell(s) from the Mind Control College, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS20
spellLink: [[Magic - Artillery Spells.pdf#page=20&search=Mass Mutilation]]
spellPoints: 1
spellTags: Artillery, Mind Control
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=20&search=Mass Mutilation|Spell Link]]

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