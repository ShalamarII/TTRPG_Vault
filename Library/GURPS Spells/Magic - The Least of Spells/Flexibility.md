---
tags:
  - Spell
  - SpellsAsMagic
spellID: pAZi3kVuxBq7lkbmK 
spellName: Flexibility
spellCollege: [Body Control]
spellDifficulty: IQ/A
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "Same"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS7
spellLink: [[Magic - The Least of Spells.pdf#page=7&search=Flexibility]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic - The Least of Spells.pdf#page=7&search=Flexibility|Spell Link]]

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