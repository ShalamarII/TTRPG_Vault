---
tags:
  - Spell
  - SpellsAsMagic
spellID: pvddUPROsDNHhAEZg 
spellName: Shape Plastic
spellCollege: [Technological]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "6"
spellMaintenance: "3"
spellPrerequisites: [6 Spell(s) from the Technological College, Shape Plant, Magery 1, Technological 1, ]
spellPrereqText: 6 Spell(s) from the Technological College, Shape Plant, Magery 1, Technological 1
spellSource: Magic
spellReference: M183
spellLink: [[Magic.pdf#page=185&search=Shape Plastic]]
spellPoints: 1
spellTags: Plastic, Technological
spellWeapons: 
---

 [[Magic.pdf#page=185&search=Shape Plastic|Spell Link]]

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