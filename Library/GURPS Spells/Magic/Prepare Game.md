---
tags:
  - Spell
  - SpellsAsMagic
spellID: pcue1V9xPKF5G5Mgi 
spellName: Prepare Game
spellCollege: [Food]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"10 sec"'
spellCost: "2"
spellMaintenance: "-"
spellPrerequisites: [Purify Food, ]
spellPrereqText: Purify Food
spellSource: Magic
spellReference: M78
spellLink: [[Magic.pdf#page=80&search=Prepare Game]]
spellPoints: 1
spellTags: Food
spellWeapons: 
---

 [[Magic.pdf#page=80&search=Prepare Game|Spell Link]]

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