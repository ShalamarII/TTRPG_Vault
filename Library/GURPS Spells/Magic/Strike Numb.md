---
tags:
  - Spell
  - SpellsAsMagic
spellID: p-8enVS-MAiJooYbC 
spellName: Strike Numb
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"10 sec"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "1"
spellPrerequisites: [Resist Pain, ]
spellPrereqText: Resist Pain
spellSource: Magic
spellReference: M40
spellLink: [[Magic.pdf#page=42&search=Strike Numb]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=42&search=Strike Numb|Spell Link]]

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