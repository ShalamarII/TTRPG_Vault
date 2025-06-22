---
tags:
  - Spell
  - SpellsAsMagic
spellID: p6xIXw638mJWZ7jGJ 
spellName: Targeted Creeping Moss
spellCollege: [Plant]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"5 Seconds"'
spellCastingTime: '"3 Sec."'
spellCost: "7"
spellMaintenance: "6"
spellPrerequisites: [Gather Moss, ]
spellPrereqText: Gather Moss
spellSource: Magic - Plant Spells
spellReference: MPS18
spellLink: [[Magic - Plant Spells.pdf#page=18&search=Targeted Creeping Moss]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=18&search=Targeted Creeping Moss|Spell Link]]

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