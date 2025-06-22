---
tags:
  - Spell
  - SpellsAsMagic
spellID: pijG6DZfZCyGhMn9L 
spellName: Fireball
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "1-Magery"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Fire 1, Shape Fire, Create Fire, ]
spellPrereqText: Magery 1, Fire 1, Shape Fire, Create Fire
spellSource: Magic
spellReference: M74
spellLink: [[Magic.pdf#page=76&search=Fireball]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"W0M_VTUU4jfZQ_HMu","damage":{"type":"burn/point","base":"1d"},"accuracy":"1","range":"25/50","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"1d burn/point"}}]
---

 [[Magic.pdf#page=76&search=Fireball|Spell Link]]

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