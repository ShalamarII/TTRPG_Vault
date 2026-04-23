---
tags:
  - Spell
  - SpellsAsMagic
spellID: pSWmu5HVeLPdgealy 
spellName: Death Ray
spellCollege: [Technological]
spellDifficulty: IQ/VH
spellClass: Missile
spellResisted: undefined
spellDuration: undefined
spellCastingTime: '"1-3 secs"'
spellCost: "2-2×Magery#"
spellMaintenance: "undefined"
spellPrerequisites: [Lightning, Radiation Jet, Magery4, ]
spellPrereqText: Lightning, Radiation Jet, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS26
spellLink: [[Magic - Artillery Spells.pdf#page=26&search=Death Ray]]
spellPoints: 1
spellTags: Artillery, Radiation, Technological
spellWeapons: [{"id":"WAkS0onjvSoYvQy8f","damage":{"type":"burn sur/2 energy","base":"1d","armor_divisor":5},"accuracy":"3","range":"50","rate_of_fire":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d(5) burn sur/2 energy"}}]
---

 [[Magic - Artillery Spells.pdf#page=26&search=Death Ray|Spell Link]]

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