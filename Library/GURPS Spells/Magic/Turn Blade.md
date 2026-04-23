---
tags:
  - Spell
  - SpellsAsMagic
spellID: pT9BKV723xZrq_L3_ 
spellName: Turn Blade
spellCollege: [Protection & Warning]
spellDifficulty: IQ/H
spellClass: Blocking
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [Apportation, Spasm, ]
spellPrereqText: Apportation, Spasm
spellSource: Magic
spellReference: M167
spellLink: [[Magic.pdf#page=169&search=Turn Blade]]
spellPoints: 1
spellTags: Protection & Warning
spellWeapons: 
---

 [[Magic.pdf#page=169&search=Turn Blade|Spell Link]]

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