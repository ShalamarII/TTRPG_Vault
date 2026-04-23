---
tags:
  - Spell
  - SpellsAsMagic
spellID: p0G1D1gx4eGbW8ZZv 
spellName: Relieve Paralysis
spellCollege: [Healing]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"10 sec"'
spellCost: "Varies"
spellMaintenance: "Same"
spellPrerequisites: [Stop Paralysis, ]
spellPrereqText: Stop Paralysis
spellSource: Magic
spellReference: M93
spellLink: [[Magic.pdf#page=95&search=Relieve Paralysis]]
spellPoints: 1
spellTags: Healing
spellWeapons: 
---

 [[Magic.pdf#page=95&search=Relieve Paralysis|Spell Link]]

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