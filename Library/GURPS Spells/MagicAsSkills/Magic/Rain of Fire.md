---
tags:
  - Spell
  - SpellsAsMagic
spellID: pNkN1cCmSE1pXmGC6 
spellName: Rain of Fire
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1#"
spellMaintenance: "Same"
spellPrerequisites: [Magery 2, Fire 2, Create Fire, ]
spellPrereqText: Magery 2, Fire 2, Create Fire
spellSource: Magic
spellReference: M74
spellLink: [[Magic.pdf#page=76&search=Rain of Fire]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"w27_EQdHf2Ismzhi0","damage":{"type":"burn","base":"1d-1"},"usage":"Area","calc":{"damage":"1d-1 burn"}}]
---

 [[Magic.pdf#page=76&search=Rain of Fire|Spell Link]]

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