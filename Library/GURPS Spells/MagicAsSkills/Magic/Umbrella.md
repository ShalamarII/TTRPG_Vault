---
tags:
  - Spell
  - SpellsAsMagic
spellID: p2o5JqSZIsK7cIxUc 
spellName: Umbrella
spellCollege: [Protection & Warning, Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"10 min"'
spellCastingTime: '"2 sec"'
spellCost: "1"
spellMaintenance: "1"
spellPrerequisites: [Shield, Shape Water, ]
spellPrereqText: Shield, Shape Water
spellSource: Magic
spellReference: M185
spellLink: [[Magic.pdf#page=187&search=Umbrella]]
spellPoints: 1
spellTags: Protection & Warning, Water
spellWeapons: 
---

 [[Magic.pdf#page=187&search=Umbrella|Spell Link]]

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