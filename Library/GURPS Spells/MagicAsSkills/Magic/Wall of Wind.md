---
tags:
  - Spell
  - SpellsAsMagic
spellID: p1syCI-LQ_j5JYebA 
spellName: Wall of Wind
spellCollege: [Air]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"Instant"'
spellCost: "2"
spellMaintenance: "Half"
spellPrerequisites: [Shape Air, ]
spellPrereqText: Shape Air
spellSource: Magic
spellReference: M25
spellLink: [[Magic.pdf#page=27&search=Wall of Wind]]
spellPoints: 1
spellTags: Air
spellWeapons: 
---

 [[Magic.pdf#page=27&search=Wall of Wind|Spell Link]]

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