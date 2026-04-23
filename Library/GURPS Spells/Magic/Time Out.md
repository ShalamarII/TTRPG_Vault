---
tags:
  - Spell
  - SpellsAsMagic
spellID: pc2lzzyh7Y4sV3i40 
spellName: Time Out
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"5 min"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Gate 3, Accelerate Time, ]
spellPrereqText: Magery 3, Gate 3, Accelerate Time
spellSource: Magic
spellReference: M87
spellLink: [[Magic.pdf#page=89&search=Time Out]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=89&search=Time Out|Spell Link]]

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