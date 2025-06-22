---
tags:
  - Spell
  - SpellsAsMagic
spellID: plbA84ysK3wLznQJO 
spellName: Disinfect
spellCollege: [Healing]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: HT
spellDuration: '"Instantaneous"'
spellCastingTime: '"1/2 base cost"'
spellCost: "2/1d"
spellMaintenance: "undefined"
spellPrerequisites: [Cure Disease, Remove Contagion, 10 Spell(s) from the Healing College, Magery4, ]
spellPrereqText: Cure Disease, Remove Contagion, 10 Spell(s) from the Healing College, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS17
spellLink: [[Magic - Artillery Spells.pdf#page=17&search=Disinfect]]
spellPoints: 1
spellTags: Artillery, Healing
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=17&search=Disinfect|Spell Link]]

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