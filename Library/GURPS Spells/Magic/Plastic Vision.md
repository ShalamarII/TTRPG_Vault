---
tags:
  - Spell
  - SpellsAsMagic
spellID: pz1zLs1xOaQSKdxK2 
spellName: Plastic Vision
spellCollege: [Knowledge, Technological]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"30 sec"'
spellCastingTime: '"1 sec"'
spellCost: "2 per 5 yd"
spellMaintenance: "Same"
spellPrerequisites: [Shape Plastic, ]
spellPrereqText: Shape Plastic
spellSource: Magic
spellReference: M183
spellLink: [[Magic.pdf#page=185&search=Plastic Vision]]
spellPoints: 1
spellTags: Knowledge, Plastic, Technological
spellWeapons: 
---

 [[Magic.pdf#page=185&search=Plastic Vision|Spell Link]]

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