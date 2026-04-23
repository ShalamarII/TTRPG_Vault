---
tags:
  - Spell
  - SpellsAsMagic
spellID: p7wUkydgkHrLktqf2 
spellName: Winged Knife
spellCollege: [Movement]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1/lb"
spellMaintenance: "-"
spellPrerequisites: [Poltergeist, ]
spellPrereqText: Poltergeist
spellSource: Magic
spellReference: M145
spellLink: [[Magic.pdf#page=147&search=Winged Knife]]
spellPoints: 1
spellTags: Movement
spellWeapons: [{"id":"WRtj7dr6tzwJdls_J","damage":{"type":"per weapon"},"accuracy":"1","range":"20/40","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Throwing"}],"calc":{"damage":"per weapon"}}]
---

 [[Magic.pdf#page=147&search=Winged Knife|Spell Link]]

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