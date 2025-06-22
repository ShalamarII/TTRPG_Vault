---
tags:
  - Spell
  - SpellsAsMagic
spellID: pzorFEdXV-iCyuEGU 
spellName: Sequence DNA
spellCollege: [Technological]
spellDifficulty: IQ/VH
spellClass: Information
spellResisted: undefined
spellDuration: '"1 week"'
spellCastingTime: '"5 min"'
spellCost: "6"
spellMaintenance: "undefined"
spellPrerequisites: [Magery 2, Technological 2, Genomancy, Analyze Heredity, ]
spellPrereqText: Magery 2, Technological 2, Genomancy, Analyze Heredity
spellSource: Bio-Tech
spellReference: BT32
spellLink: [[Bio-Tech.pdf#page=32&search=Sequence DNA]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Bio-Tech.pdf#page=32&search=Sequence DNA|Spell Link]]

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