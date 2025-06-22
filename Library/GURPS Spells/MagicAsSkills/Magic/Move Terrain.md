---
tags:
  - Spell
  - SpellsAsMagic
spellID: pHV-WgD1lqfcnWS3H 
spellName: Move Terrain
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: Special
spellDuration: '"1 hr"'
spellCastingTime: '"1 min"'
spellCost: "10"
spellMaintenance: "8"
spellPrerequisites: [Hide Object, Alter Terrain, ]
spellPrereqText: Hide Object, Alter Terrain
spellSource: Magic
spellReference: M55
spellLink: [[Magic.pdf#page=57&search=Move Terrain]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic.pdf#page=57&search=Move Terrain|Spell Link]]

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