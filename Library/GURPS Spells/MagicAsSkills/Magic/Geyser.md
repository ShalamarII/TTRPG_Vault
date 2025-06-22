---
tags:
  - Spell
  - SpellsAsMagic
spellID: pOnUQZatTUxyGEGPY 
spellName: Geyser
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"5 sec"'
spellCost: "5"
spellMaintenance: "2"
spellPrerequisites: [4 Spell(s) from the fire College, 4 Spell(s) from the Earth College, 6 Spell(s) from the Water College, Create Spring, ]
spellPrereqText: 4 Spell(s) from the fire College, 4 Spell(s) from the Earth College, 6 Spell(s) from the Water College, Create Spring
spellSource: Magic
spellReference: M190
spellLink: [[Magic.pdf#page=192&search=Geyser]]
spellPoints: 1
spellTags: Water
spellWeapons: 
---

 [[Magic.pdf#page=192&search=Geyser|Spell Link]]

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