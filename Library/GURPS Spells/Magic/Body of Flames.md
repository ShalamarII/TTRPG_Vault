---
tags:
  - Spell
  - SpellsAsMagic
spellID: pS8s-huP_WPBTi_ku 
spellName: Body of Flames
spellCollege: [Fire]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "12"
spellMaintenance: "4"
spellPrerequisites: [Breathe Fire, ]
spellPrereqText: Breathe Fire
spellSource: Magic
spellReference: M76
spellLink: [[Magic.pdf#page=78&search=Body of Flames]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"wAuUfLPEWw_PPdA73","damage":{"type":"burn","base":"1d"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Karate"}],"calc":{"damage":"1d burn"}}]
---

 [[Magic.pdf#page=78&search=Body of Flames|Spell Link]]

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