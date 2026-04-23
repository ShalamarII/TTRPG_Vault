---
tags:
  - Spell
  - SpellsAsMagic
spellID: p3MzZe9gzWsI9z9-Z 
spellName: Starbolt
spellCollege: [Light & Darkness, Technologica]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "2-6xMagery"
spellMaintenance: "-"
spellPrerequisites: [Penetrating Spell, Blackbolt, Radiation Jet, ]
spellPrereqText: Penetrating Spell, Blackbolt, Radiation Jet
spellSource: Pyramid 3 - 115
spellReference: PY115:23
spellLink: [[Pyramid 3 - 115.pdf#page=23&search=Starbolt]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: [{"id":"W5-qtkgkbmiMhxnDG","damage":{"type":"burn/2 point","base":"1d-1","armor_divisor":5},"accuracy":"2","range":"750/1,500","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d-1(5) burn/2 point"}}]
---

 [[Pyramid 3 - 115.pdf#page=23&search=Starbolt|Spell Link]]

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