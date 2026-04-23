---
tags:
  - Spell
  - SpellsAsMagic
spellID: pFQyada3rQucfguQQ 
spellName: Block
spellCollege: [Protection & Warning]
spellDifficulty: IQ/H
spellClass: Blocking
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1 per DB"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Protection & Warning 1, ]
spellPrereqText: Magery 1, Protection & Warning 1
spellSource: Magic
spellReference: M166
spellLink: [[Magic.pdf#page=168&search=Block]]
spellPoints: 1
spellTags: Protection & Warning
spellWeapons: 
---

 [[Magic.pdf#page=168&search=Block|Spell Link]]

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