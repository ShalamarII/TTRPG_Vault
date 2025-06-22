---
tags:
  - Spell
  - SpellsAsMagic
spellID: pdymRBbGVlsnqOxVq 
spellName: Improved Explosive Lightning
spellCollege: [Air, Weather]
spellDifficulty: IQ/VH
spellClass: Missile
spellResisted: undefined
spellDuration: undefined
spellCastingTime: '"1-3 secs"'
spellCost: "3-3×Magery#"
spellMaintenance: "undefined"
spellPrerequisites: [10 Spell(s) from the Air College, 10 Spell(s) from the Weather College, Explosive Lightning, Magery4, ]
spellPrereqText: 10 Spell(s) from the Air College, 10 Spell(s) from the Weather College, Explosive Lightning, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS29
spellLink: [[Magic - Artillery Spells.pdf#page=29&search=Improved Explosive Lightning]]
spellPoints: 1
spellTags: Air, Artillery, Weather
spellWeapons: [{"id":"W7CXOH84CLK3n8Isu","damage":{"type":"burn ex/3 energy","base":"1d-1"},"accuracy":"3","range":"50/100","rate_of_fire":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"1d-1 burn ex/3 energy"}}]
---

 [[Magic - Artillery Spells.pdf#page=29&search=Improved Explosive Lightning|Spell Link]]

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