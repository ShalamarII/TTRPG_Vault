---
tags:
  - Spell
  - SpellsAsMagic
spellID: pT6OUo5G93uwYcni5 
spellName: Fumble
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Blocking
spellResisted: DX
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "-"
spellPrerequisites: [Clumsiness, ]
spellPrereqText: Clumsiness
spellSource: Magic
spellReference: M38
spellLink: [[Magic.pdf#page=40&search=Fumble]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=40&search=Fumble|Spell Link]]

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