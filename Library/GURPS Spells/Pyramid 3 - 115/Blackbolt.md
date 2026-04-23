---
tags:
  - Spell
  - SpellsAsMagic
spellID: pfoqWwxiLr6pV-vSE 
spellName: Blackbolt
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "2-6xMagery"
spellMaintenance: "-"
spellPrerequisites: [6 Spell(s) from the Light & Darkness College, Sunlight, ]
spellPrereqText: 6 Spell(s) from the Light & Darkness College, Sunlight
spellSource: Pyramid 3 - 115
spellReference: PY115:20
spellLink: [[Pyramid 3 - 115.pdf#page=20&search=Blackbolt]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: [{"id":"Wxvl7rHj3OMDseko3","damage":{"type":"burn/2 point","base":"1d-1","armor_divisor":2},"accuracy":"2","range":"150/300","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d-1(2) burn/2 point"}}]
---

 [[Pyramid 3 - 115.pdf#page=20&search=Blackbolt|Spell Link]]

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