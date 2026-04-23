---
tags:
  - Spell
  - SpellsAsMagic
spellID: ph_drc0BVQKdS5ILv 
spellName: Towering Inferno
spellCollege: [Fire]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1/2 base cost"'
spellCost: "2/1d"
spellMaintenance: "undefined"
spellPrerequisites: [Rain Of Fire, 7 Spell(s) from the Fire College, Magery4, Fire Cloud, ]
spellPrereqText: Rain Of Fire, 7 Spell(s) from the Fire College, Magery4, Fire Cloud
spellSource: Magic - Artillery Spells
spellReference: MAS15
spellLink: [[Magic - Artillery Spells.pdf#page=15&search=Towering Inferno]]
spellPoints: 1
spellTags: Artillery, Fire
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=15&search=Towering Inferno|Spell Link]]

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