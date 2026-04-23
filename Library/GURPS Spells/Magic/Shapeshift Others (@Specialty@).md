---
tags:
  - Spell
  - SpellsAsMagic
spellID: p-korieXf0cMDurRW 
spellName: Shapeshift Others (@Specialty@)
spellCollege: [Animal]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: Will
spellDuration: '"1 hr"'
spellCastingTime: '"30 sec"'
spellCost: "Varies"
spellMaintenance: "Varies"
spellPrerequisites: [Magery 2, Animal 2, Shapeshifting (@Specialty@), ]
spellPrereqText: Magery 2, Animal 2, Shapeshifting (@Specialty@)
spellSource: Magic
spellReference: M33
spellLink: [[Magic.pdf#page=35&search=Shapeshift Others (@Specialty@)]]
spellPoints: 1
spellTags: Animal
spellWeapons: 
---

 [[Magic.pdf#page=35&search=Shapeshift Others (@Specialty@)|Spell Link]]

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