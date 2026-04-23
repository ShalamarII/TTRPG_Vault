---
tags:
  - Spell
  - SpellsAsMagic
spellID: pbWN92nqXnQhutHO9 
spellName: Walk Through Metal
spellCollege: [Metal]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 second"'
spellCastingTime: '"1 sec"'
spellCost: "6"
spellMaintenance: "6"
spellPrerequisites: [4 Spell(s) from the Metal College, ]
spellPrereqText: 4 Spell(s) from the Metal College
spellSource: Pyramid 3 - 91
spellReference: PY91:28
spellLink: [[Pyramid 3 - 91.pdf#page=28&search=Walk Through Metal]]
spellPoints: 1
spellTags: Metal
spellWeapons: 
---

 [[Pyramid 3 - 91.pdf#page=28&search=Walk Through Metal|Spell Link]]

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