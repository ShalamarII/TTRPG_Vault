---
tags:
  - Spell
  - SpellsAsMagic
spellID: pbMRS5c4Lp067wFbu 
spellName: Force Ball
spellCollege: [Movement, Protection & Warning]
spellDifficulty: IQ/VH
spellClass: Missile
spellResisted: undefined
spellDuration: undefined
spellCastingTime: '"1-3 secs"'
spellCost: "2-2×Magery#"
spellMaintenance: "undefined"
spellPrerequisites: [Catch Spell, Force Dome, Sense Foes, Magery4, ]
spellPrereqText: Catch Spell, Force Dome, Sense Foes, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS24
spellLink: [[Magic - Artillery Spells.pdf#page=24&search=Force Ball]]
spellPoints: 1
spellTags: Artillery, Movement, Protection & Warning
spellWeapons: [{"id":"W9a3r-Yhk8JwiiCmn","damage":{"type":"cr dkb/2 energy","base":"1d"},"accuracy":"2","range":"80","rate_of_fire":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"1d cr dkb/2 energy"}}]
---

 [[Magic - Artillery Spells.pdf#page=24&search=Force Ball|Spell Link]]

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