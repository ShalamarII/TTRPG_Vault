---
tags:
  - Spell
  - SpellsAsMagic
spellID: pms9q6pXG2fhCfahC 
spellName: Analyze Heredity
spellCollege: [Knowledge]
spellDifficulty: IQ/H
spellClass: Information
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "undefined"
spellPrerequisites: [Seeker, Sense Life, ]
spellPrereqText: Seeker, Sense Life
spellSource: Bio-Tech
spellReference: BT30
spellLink: [[Bio-Tech.pdf#page=30&search=Analyze Heredity]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Bio-Tech.pdf#page=30&search=Analyze Heredity|Spell Link]]

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