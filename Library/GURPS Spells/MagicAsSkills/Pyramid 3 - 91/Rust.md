---
tags:
  - Spell
  - SpellsAsMagic
spellID: pnSo1EYw2EfWpvgbF 
spellName: Rust
spellCollege: [Making & Breaking, Metal]
spellDifficulty: IQ/H
spellClass: Regular/R-HT-4
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "varies"
spellMaintenance: "undefined"
spellPrerequisites: [Magery 1, Making & Breaking 1, Create Metal, ]
spellPrereqText: Magery 1, Making & Breaking 1, Create Metal
spellSource: Pyramid 3 - 91
spellReference: PY91:27
spellLink: [[Pyramid 3 - 91.pdf#page=27&search=Rust]]
spellPoints: 1
spellTags: Making and Breaking, Metal
spellWeapons: 
---

 [[Pyramid 3 - 91.pdf#page=27&search=Rust|Spell Link]]

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