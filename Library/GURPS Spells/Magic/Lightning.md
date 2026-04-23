---
tags:
  - Spell
  - SpellsAsMagic
spellID: prnkk9Zj1f_vCE4z2 
spellName: Lightning
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "1-Magery"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Air 1, 6 Spell(s) from the Air College, ]
spellPrereqText: Magery 1, Air 1, 6 Spell(s) from the Air College
spellSource: Magic
spellReference: M196
spellLink: [[Magic.pdf#page=198&search=Lightning]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"WTSpbn0CBkgriggJj","damage":{"type":"burn/point","base":"1d-1"},"accuracy":"3","range":"50/100","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d-1 burn/point"}}]
---

 [[Magic.pdf#page=198&search=Lightning|Spell Link]]

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