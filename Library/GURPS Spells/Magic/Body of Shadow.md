---
tags:
  - Spell
  - SpellsAsMagic
spellID: paFF8nm8dqIjMcWO9 
spellName: Body of Shadow
spellCollege: [Light & Darkness]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "6"
spellMaintenance: "3"
spellPrerequisites: [Magery 2, Light & Darkness 2, Shape Darkness, 3 Spell(s) from the Movement College, ]
spellPrereqText: Magery 2, Light & Darkness 2, Shape Darkness, 3 Spell(s) from the Movement College
spellSource: Magic
spellReference: M114
spellLink: [[Magic.pdf#page=116&search=Body of Shadow]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Magic.pdf#page=116&search=Body of Shadow|Spell Link]]

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