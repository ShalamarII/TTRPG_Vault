---
tags:
  - Spell
  - SpellsAsMagic
spellID: pOn8AsUXA4n3OLWMj 
spellName: Slasher
spellCollege: [Movement]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"5 secs or until weapons are destroyed"'
spellCastingTime: '"1 sec/yd"'
spellCost: "2/lb"
spellMaintenance: "undefined"
spellPrerequisites: [Dancing Object, Winged Knife, 10 Spell(s) from the Movement College, Magery4, ]
spellPrereqText: Dancing Object, Winged Knife, 10 Spell(s) from the Movement College, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS22
spellLink: [[Magic - Artillery Spells.pdf#page=22&search=Slasher]]
spellPoints: 1
spellTags: Artillery, Movement
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=22&search=Slasher|Spell Link]]

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