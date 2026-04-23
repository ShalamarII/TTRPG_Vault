---
tags:
  - Spell
  - SpellsAsMagic
spellID: pfl0RCctbwk9G3geB 
spellName: Mapmaker
spellCollege: [Making & Breaking]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Inscribe, Measurement, ]
spellPrereqText: Inscribe, Measurement
spellSource: Magic
spellReference: M118
spellLink: [[Magic.pdf#page=120&search=Mapmaker]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: 
---

 [[Magic.pdf#page=120&search=Mapmaker|Spell Link]]

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