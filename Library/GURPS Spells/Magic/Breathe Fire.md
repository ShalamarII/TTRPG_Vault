---
tags:
  - Spell
  - SpellsAsMagic
spellID: pNoItCPGgkgfgRhXE 
spellName: Breathe Fire
spellCollege: [Fire]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"2 sec"'
spellCost: "1-4"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Fire 1, Resist Fire, Flame Jet, ]
spellPrereqText: Magery 1, Fire 1, Resist Fire, Flame Jet
spellSource: Magic
spellReference: M76
spellLink: [[Magic.pdf#page=78&search=Breathe Fire]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"wwuUGPxsWIhmT3gIg","damage":{"type":"burn/point","base":"1d+1"},"usage":"Breath","reach":"1","defaults":[{"type":"dx","modifier":-2},{"type":"skill","name":"Innate Attack","specialization":"Breath"}],"calc":{"damage":"1d+1 burn/point"}}]
---

 [[Magic.pdf#page=78&search=Breathe Fire|Spell Link]]

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