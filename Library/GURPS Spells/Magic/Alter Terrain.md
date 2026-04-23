---
tags:
  - Spell
  - SpellsAsMagic
spellID: pZYzeKGL4_40QnNKN 
spellName: Alter Terrain
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"2d days"'
spellCastingTime: '"10 sec"'
spellCost: "1#"
spellMaintenance: "-"
spellPrerequisites: [Shape Earth, Shape Fire, Shape Air, Shape Water, Magery 3, Earth 3, ]
spellPrereqText: Shape Earth, Shape Fire, Shape Air, Shape Water, Magery 3, Earth 3
spellSource: Magic
spellReference: M55
spellLink: [[Magic.pdf#page=57&search=Alter Terrain]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic.pdf#page=57&search=Alter Terrain|Spell Link]]

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