---
tags:
  - Spell
  - SpellsAsMagic
spellID: pOEKxxPS8I8iGiJX4 
spellName: Laser Eyes
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "1-3xMagery"
spellMaintenance: "-"
spellPrerequisites: [6 Spell(s) from the Light & Darkness College, Sunlight, ]
spellPrereqText: 6 Spell(s) from the Light & Darkness College, Sunlight
spellSource: Pyramid 3 - 115
spellReference: PY115:21
spellLink: [[Pyramid 3 - 115.pdf#page=21&search=Laser Eyes]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: [{"id":"WqrIoNm0r9nTY6V3e","damage":{"type":"burn/point","base":"1d-1"},"usage":"One Eye","accuracy":"2","range":"75/150","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Gaze"}],"calc":{"damage":"1d-1 burn/point"}},{"id":"WxQGgqgil4LKcQaOD","damage":{"type":"burn/2 points","base":"1d-1"},"usage":"Two Eyes","accuracy":"2","range":"75/150","rate_of_fire":"2","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Gaze"}],"calc":{"damage":"1d-1 burn/2 points"}}]
---

 [[Pyramid 3 - 115.pdf#page=21&search=Laser Eyes|Spell Link]]

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