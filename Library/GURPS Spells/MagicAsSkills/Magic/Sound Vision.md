---
tags:
  - Spell
  - SpellsAsMagic
spellID: pphlDqAgQLUXg_TaO 
spellName: Sound Vision
spellCollege: [Sound]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "5"
spellMaintenance: "2"
spellPrerequisites: [Acute Hearing1, Keen Hearing, ]
spellPrereqText: Acute Hearing1, Keen Hearing
spellSource: Magic
spellReference: M171
spellLink: [[Magic.pdf#page=173&search=Sound Vision]]
spellPoints: 1
spellTags: Sound
spellWeapons: 
---

 [[Magic.pdf#page=173&search=Sound Vision|Spell Link]]

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