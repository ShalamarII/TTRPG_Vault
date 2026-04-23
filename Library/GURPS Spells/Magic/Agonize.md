---
tags:
  - Spell
  - SpellsAsMagic
spellID: pgznKUPsIYYo4a7rr 
spellName: Agonize
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "8"
spellMaintenance: "6"
spellPrerequisites: [Magery 2, Body Control 2, Sensitize, ]
spellPrereqText: Magery 2, Body Control 2, Sensitize
spellSource: Magic
spellReference: M40
spellLink: [[Magic.pdf#page=42&search=Agonize]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=42&search=Agonize|Spell Link]]

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