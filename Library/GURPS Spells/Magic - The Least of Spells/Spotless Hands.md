---
tags:
  - Spell
  - SpellsAsMagic
spellID: pY5Qgm-87DWvj6TiP 
spellName: Spotless Hands
spellCollege: [Earth]
spellDifficulty: IQ/A
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 minute"'
spellCastingTime: '"2 sec"'
spellCost: "1"
spellMaintenance: "Same"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS8
spellLink: [[Magic - The Least of Spells.pdf#page=8&search=Spotless Hands]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic - The Least of Spells.pdf#page=8&search=Spotless Hands|Spell Link]]

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