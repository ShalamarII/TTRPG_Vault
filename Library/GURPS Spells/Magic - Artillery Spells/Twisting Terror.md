---
tags:
  - Spell
  - SpellsAsMagic
spellID: pB1bGhlBpS8Gaz7p7 
spellName: Twisting Terror
spellCollege: [Air]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Special"'
spellCastingTime: '"1 sec/2 base cost"'
spellCost: "2/1 yard moved"
spellMaintenance: "-"
spellPrerequisites: [Windstorm, Magery4, 10 Spell(s) from the Air College, ]
spellPrereqText: Windstorm, Magery4, 10 Spell(s) from the Air College
spellSource: Magic - Artillery Spells
spellReference: MAS10
spellLink: [[Magic - Artillery Spells.pdf#page=10&search=Twisting Terror]]
spellPoints: 1
spellTags: Air, Artillery
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=10&search=Twisting Terror|Spell Link]]

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