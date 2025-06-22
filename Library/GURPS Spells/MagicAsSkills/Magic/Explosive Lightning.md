---
tags:
  - Spell
  - SpellsAsMagic
spellID: p0oZ5Awv234yKMviv 
spellName: Explosive Lightning
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "2-2xMagery"
spellMaintenance: "-"
spellPrerequisites: [Lightning, ]
spellPrereqText: Lightning
spellSource: Magic
spellReference: M196
spellLink: [[Magic.pdf#page=198&search=Explosive Lightning]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"WpePcnnDC56ipc0aB","damage":{"type":"burn ex/2 points","base":"1d-1"},"accuracy":"3","range":"50/100","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d-1 burn ex/2 points"}}]
---

 [[Magic.pdf#page=198&search=Explosive Lightning|Spell Link]]

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