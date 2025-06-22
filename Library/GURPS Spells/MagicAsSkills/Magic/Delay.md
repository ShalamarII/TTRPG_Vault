---
tags:
  - Spell
  - SpellsAsMagic
spellID: p46cRW2ogJ5Z1VmUA 
spellName: Delay
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"2 hrs"'
spellCastingTime: '"10 sec"'
spellCost: "3"
spellMaintenance: "3"
spellPrerequisites: [Magery 3, Meta 3, ]
spellPrereqText: Magery 3, Meta 3
spellSource: Magic
spellReference: M130
spellLink: [[Magic.pdf#page=132&search=Delay]]
spellPoints: 1
spellTags: Linking, Meta
spellWeapons: 
---

 [[Magic.pdf#page=132&search=Delay|Spell Link]]

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