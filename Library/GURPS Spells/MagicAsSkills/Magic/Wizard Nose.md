---
tags:
  - Spell
  - SpellsAsMagic
spellID: p1QwN5Q6UT4TbJswk 
spellName: Wizard Nose
spellCollege: [Food, Knowledge]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "3"
spellMaintenance: "2"
spellPrerequisites: [Apportation, Far-tasting, ]
spellPrereqText: Apportation, Far-tasting
spellSource: Magic
spellReference: M104
spellLink: [[Magic.pdf#page=106&search=Wizard Nose]]
spellPoints: 1
spellTags: Food, Knowledge
spellWeapons: 
---

 [[Magic.pdf#page=106&search=Wizard Nose|Spell Link]]

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