---
tags:
  - Spell
  - SpellsAsMagic
spellID: p3avNC9391BCcyGeP 
spellName: Diminishing Dome
spellCollege: [Protection & Warning]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec"'
spellCost: "4"
spellMaintenance: "undefined"
spellPrerequisites: [Force Dome, Magery4, ]
spellPrereqText: Force Dome, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS24
spellLink: [[Magic - Artillery Spells.pdf#page=24&search=Diminishing Dome]]
spellPoints: 1
spellTags: Artillery, Protection & Warning
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=24&search=Diminishing Dome|Spell Link]]

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