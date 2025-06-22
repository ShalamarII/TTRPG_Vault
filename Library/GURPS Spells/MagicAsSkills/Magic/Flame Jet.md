---
tags:
  - Spell
  - SpellsAsMagic
spellID: pm-qdngq2RTbpBsc5 
spellName: Flame Jet
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec"'
spellCost: "1-3"
spellMaintenance: "Same"
spellPrerequisites: [Create Fire, Shape Fire, ]
spellPrereqText: Create Fire, Shape Fire
spellSource: Magic
spellReference: M73
spellLink: [[Magic.pdf#page=75&search=Flame Jet]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"wl7SPGQpsAS8kVuaT","damage":{"type":"burn/point","base":"1d"},"usage":"Jet","reach":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d burn/point"}}]
---

 [[Magic.pdf#page=75&search=Flame Jet|Spell Link]]

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