---
tags:
  - Spell
  - SpellsAsMagic
spellID: pNijWMuu56ulOOO8G 
spellName: Total Paralysis
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Melee
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Paralyze Limb, ]
spellPrereqText: Paralyze Limb
spellSource: Magic
spellReference: M40
spellLink: [[Magic.pdf#page=42&search=Total Paralysis]]
spellPoints: 1
spellTags: Body Control
spellWeapons: [{"id":"wk5pDPexQL_bB3bnC","damage":{"type":"cr + Paralysis","st":"thr","base":"-1"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Karate"}],"calc":{"damage":"thr-1 cr + Paralysis"}}]
---

 [[Magic.pdf#page=42&search=Total Paralysis|Spell Link]]

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