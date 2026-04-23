---
tags:
  - Spell
  - SpellsAsMagic
spellID: pxjb3hhh_ssi3YRj3 
spellName: Blur
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "1-5"
spellMaintenance: "Same"
spellPrerequisites: [Darkness, Gloom, ]
spellPrereqText: Darkness, Gloom
spellSource: Magic
spellReference: M113
spellLink: [[Magic.pdf#page=115&search=Blur]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Magic.pdf#page=115&search=Blur|Spell Link]]

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