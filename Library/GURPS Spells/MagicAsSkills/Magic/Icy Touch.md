---
tags:
  - Spell
  - SpellsAsMagic
spellID: pa8rVeiGc3KlPh0Df 
spellName: Icy Touch
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Melee
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec#"'
spellCost: "2#"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Water 1, 4 Spell(s) from the Water College, ]
spellPrereqText: Magery 1, Water 1, 4 Spell(s) from the Water College
spellSource: Magic
spellReference: M188
spellLink: [[Magic.pdf#page=190&search=Icy Touch]]
spellPoints: 1
spellTags: Water
spellWeapons: [{"id":"wEDSsXXz_ywrV9wr8","damage":{"type":"+paralysis","st":"thr","base":"-1"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Karate"}],"calc":{"damage":"thr-1 +paralysis"}}]
---

 [[Magic.pdf#page=190&search=Icy Touch|Spell Link]]

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