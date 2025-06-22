---
tags:
  - Spell
  - SpellsAsMagic
spellID: pJGRZDGJ3c58hO7kc 
spellName: Explosive Mine
spellCollege: [Making & Breaking]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 minute or triggered"'
spellCastingTime: '"1-3 secs"'
spellCost: "4/1d"
spellMaintenance: "undefined"
spellPrerequisites: [10 Spell(s) from the Making & Breaking College, Explode, Magery3, ]
spellPrereqText: 10 Spell(s) from the Making & Breaking College, Explode, Magery3
spellSource: Magic - Artillery Spells
spellReference: MAS19
spellLink: [[Magic - Artillery Spells.pdf#page=19&search=Explosive Mine]]
spellPoints: 1
spellTags: Artillery, Making & Breaking
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=19&search=Explosive Mine|Spell Link]]

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