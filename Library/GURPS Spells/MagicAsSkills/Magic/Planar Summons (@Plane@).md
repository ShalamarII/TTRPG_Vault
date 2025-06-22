---
tags:
  - Spell
  - SpellsAsMagic
spellID: pkfCTPDdY-ssxzy_K 
spellName: Planar Summons (@Plane@)
spellCollege: [Gate]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"5 min"'
spellCost: "20#"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Gate 1, 1 Spell(s) from 10 Colleges, ]
spellPrereqText: Magery 1, Gate 1, 1 Spell(s) from 10 Colleges
spellSource: Magic
spellReference: M82
spellLink: [[Magic.pdf#page=84&search=Planar Summons (@Plane@)]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=84&search=Planar Summons (@Plane@)|Spell Link]]

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