---
tags:
  - Spell
  - SpellsAsMagic
spellID: pt-9BmVL5ZbwIOciX 
spellName: Restore Metal
spellCollege: [Making & Breaking, Metal]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "5/pound"
spellMaintenance: "undefined"
spellPrerequisites: [Rust, ]
spellPrereqText: Rust
spellSource: Pyramid 3 - 91
spellReference: PY91:26
spellLink: [[Pyramid 3 - 91.pdf#page=26&search=Restore Metal]]
spellPoints: 1
spellTags: Making & Breaking, Metal
spellWeapons: 
---

 [[Pyramid 3 - 91.pdf#page=26&search=Restore Metal|Spell Link]]

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