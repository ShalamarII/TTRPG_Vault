---
tags:
  - Spell
  - SpellsAsMagic
spellID: pKk7xtWVvo1fSZhOk 
spellName: Stiffen
spellCollege: [Making & Breaking]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Special
spellDuration: '"10 min"'
spellCastingTime: '"2 sec/lb"'
spellCost: "1/lb"
spellMaintenance: "Half"
spellPrerequisites: [Rejoin, ]
spellPrereqText: Rejoin
spellSource: Magic
spellReference: M117
spellLink: [[Magic.pdf#page=119&search=Stiffen]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: 
---

 [[Magic.pdf#page=119&search=Stiffen|Spell Link]]

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