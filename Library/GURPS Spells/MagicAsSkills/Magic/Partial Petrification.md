---
tags:
  - Spell
  - SpellsAsMagic
spellID: pq6JjBUxScyG2l6Dj 
spellName: Partial Petrification
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Permanent"'
spellCastingTime: '"2 sec"'
spellCost: "12"
spellMaintenance: "-"
spellPrerequisites: [Magery 2, Earth 2, Flesh To Stone, ]
spellPrereqText: Magery 2, Earth 2, Flesh To Stone
spellSource: Magic
spellReference: M52
spellLink: [[Magic.pdf#page=54&search=Partial Petrification]]
spellPoints: 1
spellTags: Earth
spellWeapons: [{"id":"wd06Sg9kc7iBJRDv8","damage":{"type":"Petrification"},"usage":"Punch","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Boxing"},{"type":"skill","name":"Brawling"},{"type":"skill","name":"Karate"}],"calc":{"damage":"Petrification"}}]
---

 [[Magic.pdf#page=54&search=Partial Petrification|Spell Link]]

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