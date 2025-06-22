---
tags:
  - Spell
  - SpellsAsMagic
spellID: pZooRUJ7HdRCNZ1j5 
spellName: Remove Aura
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Special
spellDuration: '"Permanent"'
spellCastingTime: '"10 sec"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Aura, Dispel Magic, ]
spellPrereqText: Aura, Dispel Magic
spellSource: Magic
spellReference: M127
spellLink: [[Magic.pdf#page=129&search=Remove Aura]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=129&search=Remove Aura|Spell Link]]

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