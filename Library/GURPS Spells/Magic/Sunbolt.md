---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVC_Drb55Mzl5Wil6 
spellName: Sunbolt
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
spellSource: Magic
spellReference: M114
spellLink: [[Magic.pdf#page=116&search=Sunbolt]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: [{"id":"W0VUInYTToZXEo_BK","damage":{"type":"imp/point","base":"1d-1"},"accuracy":"2","range":"75/150","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d-1 imp/point"}}]
---

 [[Magic.pdf#page=116&search=Sunbolt|Spell Link]]

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