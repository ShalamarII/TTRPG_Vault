---
tags:
  - Spell
  - SpellsAsMagic
spellID: pSrfW0DMHvSmn_S9e 
spellName: Crushing Fist
spellCollege: [Movement]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "undefined"
spellPrerequisites: [Distant Blow, Wizard Hand, 10 Spell(s) from the Movement College, Magery4, ]
spellPrereqText: Distant Blow, Wizard Hand, 10 Spell(s) from the Movement College, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS21
spellLink: [[Magic - Artillery Spells.pdf#page=21&search=Crushing Fist]]
spellPoints: 1
spellTags: Artillery, Movement
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=21&search=Crushing Fist|Spell Link]]

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