---
tags:
  - Spell
  - SpellsAsMagic
spellID: pR9nxUErKCE-lwTsT 
spellName: Resist Pain
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Magery 2, Body Control 2, Pain, ]
spellPrereqText: Magery 2, Body Control 2, Pain
spellSource: Magic
spellReference: M38
spellLink: [[Magic.pdf#page=40&search=Resist Pain]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=40&search=Resist Pain|Spell Link]]

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