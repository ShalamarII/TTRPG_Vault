---
tags:
  - Spell
  - SpellsAsMagic
spellID: p_i84WOYU9C9ws0hU 
spellName: Master
spellCollege: [Animal]
spellDifficulty: IQ/H
spellClass: Regular or Blocking
spellResisted: IQ
spellDuration: '"Indefinite"'
spellCastingTime: '"1 sec"'
spellCost: "2"
spellMaintenance: "-"
spellPrerequisites: [Beast Soother, ]
spellPrereqText: Beast Soother
spellSource: Magic
spellReference: M30
spellLink: [[Magic.pdf#page=32&search=Master]]
spellPoints: 1
spellTags: Animal
spellWeapons: 
---

 [[Magic.pdf#page=32&search=Master|Spell Link]]

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