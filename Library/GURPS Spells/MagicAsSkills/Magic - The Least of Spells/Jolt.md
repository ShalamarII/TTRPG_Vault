---
tags:
  - Spell
  - SpellsAsMagic
spellID: pvK29u_RHI4qK4r-i 
spellName: Jolt
spellCollege: [Air, Weather]
spellDifficulty: IQ/A
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS17
spellLink: [[Magic - The Least of Spells.pdf#page=17&search=Jolt]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"WMl8OLCZN9ddihf_l","damage":{"type":"HT+1 aff"},"range":"5/10","defaults":[{"type":"skill","name":"Innate Attack","specialization":"Projectile"},{"type":"dx","modifier":-4}],"calc":{"damage":"HT+1 aff"}}]
---

 [[Magic - The Least of Spells.pdf#page=17&search=Jolt|Spell Link]]

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