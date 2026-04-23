---
tags:
  - Spell
  - SpellsAsMagic
spellID: pL-OPG-5_fSLn-lIg 
spellName: Malfunction
spellCollege: [Technological]
spellDifficulty: IQ/H
spellClass: Melee
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Glitch, Magery 2, Technological 2, ]
spellPrereqText: Glitch, Magery 2, Technological 2
spellSource: Magic
spellReference: M177
spellLink: [[Magic.pdf#page=179&search=Malfunction]]
spellPoints: 1
spellTags: Machine, Technological
spellWeapons: 
---

 [[Magic.pdf#page=179&search=Malfunction|Spell Link]]

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