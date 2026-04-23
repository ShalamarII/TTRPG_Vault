---
tags:
  - Spell
  - SpellsAsMagic
spellID: pIXGxpFac-yStZQTc 
spellName: Lightning Whip
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 sec"'
spellCastingTime: '"2 sec"'
spellCost: "1 per 2 yards"
spellMaintenance: "Same"
spellPrerequisites: [Lightning, ]
spellPrereqText: Lightning
spellSource: Magic
spellReference: M196
spellLink: [[Magic.pdf#page=198&search=Lightning Whip]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"wvuxmbnuKUuTl0KTG","damage":{"type":"burn","base":"1d"},"reach":"2","defaults":[{"type":"dx","modifier":-5},{"type":"skill","name":"Whip"},{"type":"skill","name":"Kusari","modifier":-3},{"type":"skill","name":"Monowire Whip","modifier":-3}],"calc":{"damage":"1d burn"}}]
---

 [[Magic.pdf#page=198&search=Lightning Whip|Spell Link]]

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