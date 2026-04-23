---
tags:
  - Spell
  - SpellsAsMagic
spellID: ploL58IEacHO1GWAc 
spellName: Rain of Ice Daggers
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "2#"
spellMaintenance: "Same"
spellPrerequisites: [Ice Dagger, Hail, Magery 2, Water 2, ]
spellPrereqText: Ice Dagger, Hail, Magery 2, Water 2
spellSource: Magic
spellReference: M192
spellLink: [[Magic.pdf#page=194&search=Rain of Ice Daggers]]
spellPoints: 1
spellTags: Water
spellWeapons: [{"id":"wyrcb96rftIb-EZsP","damage":{"type":"imp","base":"1d-2"},"usage":"Area","calc":{"damage":"1d-2 imp"}}]
---

 [[Magic.pdf#page=194&search=Rain of Ice Daggers|Spell Link]]

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