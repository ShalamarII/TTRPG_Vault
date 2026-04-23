---
tags:
  - Spell
  - SpellsAsMagic
spellID: pP5PDZMC_VX2OhzNI 
spellName: Seismic Shock
spellCollege: [Earth]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 sec"'
spellCost: "8"
spellMaintenance: "undefined"
spellPrerequisites: [1 Spell(s) from the Earth College, Earthquake, Magery4, ]
spellPrereqText: 1 Spell(s) from the Earth College, Earthquake, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS13
spellLink: [[Magic - Artillery Spells.pdf#page=13&search=Seismic Shock]]
spellPoints: 1
spellTags: Artillery, Earth
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=13&search=Seismic Shock|Spell Link]]

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