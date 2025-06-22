---
tags:
  - Spell
  - SpellsAsMagic
spellID: pyCYc1fejvKoKMMse 
spellName: Concussion
spellCollege: [Air, Sound]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "2-2xMagery"
spellMaintenance: "-"
spellPrerequisites: [Shape Air, Thunderclap, ]
spellPrereqText: Shape Air, Thunderclap
spellSource: Magic
spellReference: M26
spellLink: [[Magic.pdf#page=28&search=Concussion]]
spellPoints: 1
spellTags: Air, Sound
spellWeapons: [{"id":"WKcztfQgVmPD-rXRX","damage":{"type":"cr ex/2 points","base":"1d"},"accuracy":"1","range":"20/40","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"1d cr ex/2 points"}}]
---

 [[Magic.pdf#page=28&search=Concussion|Spell Link]]

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