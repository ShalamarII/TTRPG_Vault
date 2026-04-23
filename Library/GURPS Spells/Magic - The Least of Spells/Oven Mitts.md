---
tags:
  - Spell
  - SpellsAsMagic
spellID: p6gNFVGSgQjF0un-9 
spellName: Oven Mitts
spellCollege: [Fire, Protection & Warning]
spellDifficulty: IQ/A
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 minute"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "Same"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS9
spellLink: [[Magic - The Least of Spells.pdf#page=9&search=Oven Mitts]]
spellPoints: 1
spellTags: Fire, Protection & Warning
spellWeapons: 
---

 [[Magic - The Least of Spells.pdf#page=9&search=Oven Mitts|Spell Link]]

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