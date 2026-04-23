---
tags:
  - Spell
  - SpellsAsMagic
spellID: p-YZmO37QTaNNrTDT 
spellName: Shade
spellCollege: [Protection & Warning]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "1"
spellMaintenance: "Half"
spellPrerequisites: [Continual Light, Shield, ]
spellPrereqText: Continual Light, Shield
spellSource: Magic
spellReference: M169
spellLink: [[Magic.pdf#page=171&search=Shade]]
spellPoints: 1
spellTags: Protection & Warning
spellWeapons: 
---

 [[Magic.pdf#page=171&search=Shade|Spell Link]]

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