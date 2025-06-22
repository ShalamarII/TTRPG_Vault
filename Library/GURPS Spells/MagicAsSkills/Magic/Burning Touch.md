---
tags:
  - Spell
  - SpellsAsMagic
spellID: pTbRYYb42lMkJTZZ9 
spellName: Burning Touch
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Melee
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1-3"
spellMaintenance: "-"
spellPrerequisites: [Magery 2, Fire 2, 5 Spell(s) from the Fire College, Heat, ]
spellPrereqText: Magery 2, Fire 2, 5 Spell(s) from the Fire College, Heat
spellSource: Magic
spellReference: M76
spellLink: [[Magic.pdf#page=78&search=Burning Touch]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"wydq5liBm_y_SygVk","damage":{"type":"+1d burn/point","st":"thr","base":"-1"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Karate"}],"calc":{"damage":"thr-1 +1d burn/point"}}]
---

 [[Magic.pdf#page=78&search=Burning Touch|Spell Link]]

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