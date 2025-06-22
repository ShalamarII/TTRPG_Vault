---
tags:
  - Spell
  - SpellsAsMagic
spellID: piFY0HJwVCWcV-yXy 
spellName: Partial Shapeshifting
spellCollege: [Animal]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "Varies"
spellMaintenance: "Varies"
spellPrerequisites: [Magery 3, Animal 3, Alter Body, Shapeshift Others, ]
spellPrereqText: Magery 3, Animal 3, Alter Body, Shapeshift Others
spellSource: Magic
spellReference: M34
spellLink: [[Magic.pdf#page=36&search=Partial Shapeshifting]]
spellPoints: 1
spellTags: Animal
spellWeapons: 
---

 [[Magic.pdf#page=36&search=Partial Shapeshifting|Spell Link]]

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