---
tags:
  - Spell
  - SpellsAsMagic
spellID: pwli8lNPKhw0ZZkr- 
spellName: Machine Summoning
spellCollege: [Technological]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"4 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Machine Control, ]
spellPrereqText: Machine Control
spellSource: Magic
spellReference: M176
spellLink: [[Magic.pdf#page=178&search=Machine Summoning]]
spellPoints: 1
spellTags: Machine, Technological
spellWeapons: 
---

 [[Magic.pdf#page=178&search=Machine Summoning|Spell Link]]

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