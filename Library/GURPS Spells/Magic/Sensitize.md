---
tags:
  - Spell
  - SpellsAsMagic
spellID: pyC8KfBiMc15BS7xQ 
spellName: Sensitize
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "2"
spellPrerequisites: [Magery 1, Body Control 1, Stun, ]
spellPrereqText: Magery 1, Body Control 1, Stun
spellSource: Magic
spellReference: M39
spellLink: [[Magic.pdf#page=41&search=Sensitize]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=41&search=Sensitize|Spell Link]]

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