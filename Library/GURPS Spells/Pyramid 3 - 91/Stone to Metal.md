---
tags:
  - Spell
  - SpellsAsMagic
spellID: pHM8qAr76Nhw5Ckym 
spellName: Stone to Metal
spellCollege: [Earth, Metal]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec"'
spellCost: "3/cubic yard (min 3)"
spellMaintenance: "-"
spellPrerequisites: [Magery 2, Earth 2, Shape Metal, ]
spellPrereqText: Magery 2, Earth 2, Shape Metal
spellSource: Pyramid 3 - 91
spellReference: PY91:27
spellLink: [[Pyramid 3 - 91.pdf#page=27&search=Stone to Metal]]
spellPoints: 1
spellTags: Earth, Metal
spellWeapons: 
---

 [[Pyramid 3 - 91.pdf#page=27&search=Stone to Metal|Spell Link]]

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