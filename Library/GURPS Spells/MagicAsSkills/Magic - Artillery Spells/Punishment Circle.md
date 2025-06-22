---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVKzUV55sLy1YFdos 
spellName: Punishment Circle
spellCollege: [Meta, Necromancy]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"1 minute"'
spellCastingTime: '"1 sec/yard"'
spellCost: "3"
spellMaintenance: "Same"
spellPrerequisites: [Pentagram, Repel Spirits, Magery3, ]
spellPrereqText: Pentagram, Repel Spirits, Magery3
spellSource: Magic - Artillery Spells
spellReference: MAS19
spellLink: [[Magic - Artillery Spells.pdf#page=19&search=Punishment Circle]]
spellPoints: 1
spellTags: Artillery, Meta, Necromancy
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=19&search=Punishment Circle|Spell Link]]

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