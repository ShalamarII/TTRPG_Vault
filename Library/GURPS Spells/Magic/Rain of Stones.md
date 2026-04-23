---
tags:
  - Spell
  - SpellsAsMagic
spellID: pxLFWDXuCbWj2NOHE 
spellName: Rain of Stones
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1#"
spellMaintenance: "Same"
spellPrerequisites: [Magery 2, Earth 2, Create Earth, ]
spellPrereqText: Magery 2, Earth 2, Create Earth
spellSource: Magic
spellReference: M53
spellLink: [[Magic.pdf#page=55&search=Rain of Stones]]
spellPoints: 1
spellTags: Earth
spellWeapons: [{"id":"wRvIj3SefNYYM1_3L","damage":{"type":"cr/point","base":"1d-1"},"usage":"Area","calc":{"damage":"1d-1 cr/point"}}]
---

 [[Magic.pdf#page=55&search=Rain of Stones|Spell Link]]

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