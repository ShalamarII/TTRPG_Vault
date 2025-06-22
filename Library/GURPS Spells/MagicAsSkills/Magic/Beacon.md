---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBCxu3y0bEd0rgRYT 
spellName: Beacon
spellCollege: [Gate, Movement]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"24 hrs"'
spellCastingTime: '"30 sec"'
spellCost: "10"
spellMaintenance: "Half"
spellPrerequisites: [Timeport, Teleport, Plane Shift, ]
spellPrereqText: Timeport, Teleport, Plane Shift
spellSource: Magic
spellReference: M83
spellLink: [[Magic.pdf#page=85&search=Beacon]]
spellPoints: 1
spellTags: Gate, Movement
spellWeapons: 
---

 [[Magic.pdf#page=85&search=Beacon|Spell Link]]

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