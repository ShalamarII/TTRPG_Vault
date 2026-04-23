---
tags:
  - Spell
  - SpellsAsMagic
spellID: pwAT-Z6e2FM0_AGZR 
spellName: Dull Taste and Smell
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"30 min"'
spellCastingTime: '"1 sec"'
spellCost: "1/2 pts decrease"
spellMaintenance: "Half"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic
spellReference: M133
spellLink: [[Magic.pdf#page=135&search=Dull Taste and Smell]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=135&search=Dull Taste and Smell|Spell Link]]

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