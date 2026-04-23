---
tags:
  - Spell
  - SpellsAsMagic
spellID: pP4-7RBQaO9v4RwA3 
spellName: Compel Truth
spellCollege: [Communication & Empathy]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: Will
spellDuration: '"5 min"'
spellCastingTime: '"1 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Magery 2, Communication & Empathy 2, Truthsayer, ]
spellPrereqText: Magery 2, Communication & Empathy 2, Truthsayer
spellSource: Magic
spellReference: M47
spellLink: [[Magic.pdf#page=49&search=Compel Truth]]
spellPoints: 1
spellTags: Communication & Empathy
spellWeapons: 
---

 [[Magic.pdf#page=49&search=Compel Truth|Spell Link]]

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