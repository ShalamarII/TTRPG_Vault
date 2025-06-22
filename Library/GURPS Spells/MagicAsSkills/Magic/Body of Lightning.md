---
tags:
  - Spell
  - SpellsAsMagic
spellID: pRf9V4HkV3k8NJCAb 
spellName: Body of Lightning
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "12"
spellMaintenance: "4"
spellPrerequisites: [Lightning, Magery 2, Air 2, ]
spellPrereqText: Lightning, Magery 2, Air 2
spellSource: Magic
spellReference: M198
spellLink: [[Magic.pdf#page=200&search=Body of Lightning]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"wxbywwHxaGEj3hW4z","damage":{"type":"burn","base":"1d"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Karate"}],"calc":{"damage":"1d burn"}}]
---

 [[Magic.pdf#page=200&search=Body of Lightning|Spell Link]]

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