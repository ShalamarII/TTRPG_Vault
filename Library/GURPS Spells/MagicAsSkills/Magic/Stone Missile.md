---
tags:
  - Spell
  - SpellsAsMagic
spellID: pzkbexPz8EU_ir8MU 
spellName: Stone Missile
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "1-Magery"
spellMaintenance: "-"
spellPrerequisites: [Create Earth, ]
spellPrereqText: Create Earth
spellSource: Magic
spellReference: M52
spellLink: [[Magic.pdf#page=54&search=Stone Missile]]
spellPoints: 1
spellTags: Earth
spellWeapons: [{"id":"W-IOs9cQLYat8Sjiv","damage":{"type":"cr/point","base":"1d+1"},"accuracy":"2","range":"40/80","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"1d+1 cr/point"}}]
---

 [[Magic.pdf#page=54&search=Stone Missile|Spell Link]]

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