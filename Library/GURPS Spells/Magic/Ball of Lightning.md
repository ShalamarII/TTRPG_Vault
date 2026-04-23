---
tags:
  - Spell
  - SpellsAsMagic
spellID: puyLHSmL_FaUpjtB2 
spellName: Ball of Lightning
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1-3 sec"'
spellCost: "2-6"
spellMaintenance: "Half"
spellPrerequisites: [Lightning, Apportation, ]
spellPrereqText: Lightning, Apportation
spellSource: Magic
spellReference: M197
spellLink: [[Magic.pdf#page=199&search=Ball of Lightning]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"wnFkDxMfxSElH6Ael","damage":{"type":"burn ex/point","base":"1d-1"},"calc":{"damage":"1d-1 burn ex/point"}}]
---

 [[Magic.pdf#page=199&search=Ball of Lightning|Spell Link]]

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