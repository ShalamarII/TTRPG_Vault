---
tags:
  - Spell
  - SpellsAsMagic
spellID: pXeaDYg4NbPRmhjkf 
spellName: Steelwraith
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "7"
spellMaintenance: "4"
spellPrerequisites: [Magery 2, Earth 2, Walk Through Earth, ]
spellPrereqText: Magery 2, Earth 2, Walk Through Earth
spellSource: Magic
spellReference: M54
spellLink: [[Magic.pdf#page=56&search=Steelwraith]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic.pdf#page=56&search=Steelwraith|Spell Link]]

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