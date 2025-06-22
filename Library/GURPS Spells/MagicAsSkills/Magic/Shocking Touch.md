---
tags:
  - Spell
  - SpellsAsMagic
spellID: pY70taLLub6swp4iN 
spellName: Shocking Touch
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Melee
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1-3"
spellMaintenance: "-"
spellPrerequisites: [Lightning, ]
spellPrereqText: Lightning
spellSource: Magic
spellReference: M196
spellLink: [[Magic.pdf#page=198&search=Shocking Touch]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"wiqxntOGXnplu4ipr","damage":{"type":"cr +1d+1 burn/point","st":"thr","base":"-1"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Karate"}],"calc":{"damage":"thr-1 cr +1d+1 burn/point"}}]
---

 [[Magic.pdf#page=198&search=Shocking Touch|Spell Link]]

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