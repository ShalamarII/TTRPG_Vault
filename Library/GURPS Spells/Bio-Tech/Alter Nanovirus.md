---
tags:
  - Spell
  - SpellsAsMagic
spellID: pPnFhNnOuqcwprv34 
spellName: Alter Nanovirus
spellCollege: [Technological]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "10*(MAX(9,TL)-8)"
spellMaintenance: "undefined"
spellPrerequisites: [Manipulate DNA, Sense Nano, ]
spellPrereqText: Manipulate DNA, Sense Nano
spellSource: Bio-Tech
spellReference: BT30
spellLink: [[Bio-Tech.pdf#page=30&search=Alter Nanovirus]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Bio-Tech.pdf#page=30&search=Alter Nanovirus|Spell Link]]

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