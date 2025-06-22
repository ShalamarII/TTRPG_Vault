---
tags:
  - Spell
  - SpellsAsMagic
spellID: pqfh40X_vXrqzJ8FN 
spellName: Permanent Machine Possession
spellCollege: [Technological]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"Indefinite"'
spellCastingTime: '"5 min"'
spellCost: "30"
spellMaintenance: "-"
spellPrerequisites: [Machine Possession, Magery 3, Technological 3, ]
spellPrereqText: Machine Possession, Magery 3, Technological 3
spellSource: Magic
spellReference: M178
spellLink: [[Magic.pdf#page=180&search=Permanent Machine Possession]]
spellPoints: 1
spellTags: Machine, Technological
spellWeapons: 
---

 [[Magic.pdf#page=180&search=Permanent Machine Possession|Spell Link]]

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