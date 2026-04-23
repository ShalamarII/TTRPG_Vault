---
tags:
  - Spell
  - SpellsAsMagic
spellID: pLPefUneAlLnn_MCc 
spellName: Poltergeist
spellCollege: [Movement]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1 or 2"
spellMaintenance: "-"
spellPrerequisites: [Apportation, ]
spellPrereqText: Apportation
spellSource: Magic
spellReference: M144
spellLink: [[Magic.pdf#page=146&search=Poltergeist]]
spellPoints: 1
spellTags: Movement
spellWeapons: [{"id":"WQUfiOTHSDfUKZ-Ks","damage":{"type":"Special cr"},"accuracy":"1","range":"20/60","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Throwing"}],"calc":{"damage":"Special cr"}}]
---

 [[Magic.pdf#page=146&search=Poltergeist|Spell Link]]

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