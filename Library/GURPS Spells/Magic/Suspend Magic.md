---
tags:
  - Spell
  - SpellsAsMagic
spellID: pl7VY-OYeJtkqR_8Y 
spellName: Suspend Magic
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: Subject spells
spellDuration: '"1 min"'
spellCastingTime: '"1 sec/pt"'
spellCost: "3"
spellMaintenance: "2"
spellPrerequisites: [at least 8 Spells, Suspend Spell, ]
spellPrereqText: at least 8 Spells, Suspend Spell
spellSource: Magic
spellReference: M123
spellLink: [[Magic.pdf#page=125&search=Suspend Magic]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=125&search=Suspend Magic|Spell Link]]

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