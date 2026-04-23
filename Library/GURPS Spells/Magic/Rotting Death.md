---
tags:
  - Spell
  - SpellsAsMagic
spellID: pwNaRI8F9f4jQoYGP 
spellName: Rotting Death
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Melee
spellResisted: HT
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "2"
spellPrerequisites: [Magery 2, Necromancy 2, Sickness, Pestilence, ]
spellPrereqText: Magery 2, Necromancy 2, Sickness, Pestilence
spellSource: Magic
spellReference: M154
spellLink: [[Magic.pdf#page=156&search=Rotting Death]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: [{"id":"wEoqj62KuPo9k6plY","damage":{"type":"cr +1d-1 tox/second","st":"thr","base":"-1"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Karate"}],"calc":{"damage":"thr-1 cr +1d-1 tox/second"}}]
---

 [[Magic.pdf#page=156&search=Rotting Death|Spell Link]]

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