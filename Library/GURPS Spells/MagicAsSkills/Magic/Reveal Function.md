---
tags:
  - Spell
  - SpellsAsMagic
spellID: p0awCKDs9JO3S7UFB 
spellName: Reveal Function
spellCollege: [Technological]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: Spells to conceal magic
spellDuration: '"Instant"'
spellCastingTime: '"10 min"'
spellCost: "8"
spellMaintenance: "-"
spellPrerequisites: [Seek Machine, ]
spellPrereqText: Seek Machine
spellSource: Magic
spellReference: M176
spellLink: [[Magic.pdf#page=178&search=Reveal Function]]
spellPoints: 1
spellTags: Machine, Technological
spellWeapons: 
---

 [[Magic.pdf#page=178&search=Reveal Function|Spell Link]]

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