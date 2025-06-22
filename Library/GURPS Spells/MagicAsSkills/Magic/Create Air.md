---
tags:
  - Spell
  - SpellsAsMagic
spellID: pID_KoeYb8yT5tsEd 
spellName: Create Air
spellCollege: [Air]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"5 sec"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [Purify Air, Seek Air, ]
spellPrereqText: Purify Air, Seek Air
spellSource: Magic
spellReference: M23
spellLink: [[Magic.pdf#page=25&search=Create Air]]
spellPoints: 1
spellTags: Air
spellWeapons: 
---

 [[Magic.pdf#page=25&search=Create Air|Spell Link]]

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