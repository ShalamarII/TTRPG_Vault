---
tags:
  - Spell
  - SpellsAsMagic
spellID: pU6YI3cS7tdwIjZiU 
spellName: Minefield
spellCollege: [Making & Breaking]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"1 minute or minefield cleared"'
spellCastingTime: '"1 sec/1d"'
spellCost: "2-4×Magery"
spellMaintenance: "undefined"
spellPrerequisites: [Explosive Mine, Magery4, ]
spellPrereqText: Explosive Mine, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS19
spellLink: [[Magic - Artillery Spells.pdf#page=19&search=Minefield]]
spellPoints: 1
spellTags: Artillery, Making & Breaking
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=19&search=Minefield|Spell Link]]

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