---
tags:
  - Spell
  - SpellsAsMagic
spellID: pFOa4OaSns3uo9bSk 
spellName: Abominable Alteration
spellCollege: [Animal]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT or Will
spellDuration: '"Instant"'
spellCastingTime: '"10 sec"'
spellCost: "11"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Animal 3, Shapeshift Others, Alter Body, ]
spellPrereqText: Magery 3, Animal 3, Shapeshift Others, Alter Body
spellSource: Magic - Death Spells
spellReference: MDS9
spellLink: [[Magic - Death Spells.pdf#page=9&search=Abominable Alteration]]
spellPoints: 1
spellTags: Animal
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=9&search=Abominable Alteration|Spell Link]]

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