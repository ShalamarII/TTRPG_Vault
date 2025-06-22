---
tags:
  - Spell
  - SpellsAsMagic
spellID: pMuBa-2JN88sERUZI 
spellName: Fire Cloud
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"10 sec"'
spellCastingTime: '"1-5 sec"'
spellCost: "1-5"
spellMaintenance: "Same"
spellPrerequisites: [Fireball, Shape Air, ]
spellPrereqText: Fireball, Shape Air
spellSource: Magic
spellReference: M75
spellLink: [[Magic.pdf#page=77&search=Fire Cloud]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"w0I7hOdcKrdFFJSUY","damage":{"type":"point burn/point","base":"1"},"usage":"Area","calc":{"damage":"1 point burn/point"}}]
---

 [[Magic.pdf#page=77&search=Fire Cloud|Spell Link]]

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