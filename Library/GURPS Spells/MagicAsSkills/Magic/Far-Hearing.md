---
tags:
  - Spell
  - SpellsAsMagic
spellID: pElb5ESkutNaKWKzY 
spellName: Far-Hearing
spellCollege: [Sound]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"3 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [4 Spell(s) from the Sound College, Does not have Hard Of Hearing, Does not have Deafness, Magery 1, Sound 1, ]
spellPrereqText: 4 Spell(s) from the Sound College, Does not have Hard Of Hearing, Does not have Deafness, Magery 1, Sound 1
spellSource: Magic
spellReference: M173
spellLink: [[Magic.pdf#page=175&search=Far-Hearing]]
spellPoints: 1
spellTags: Sound
spellWeapons: 
---

 [[Magic.pdf#page=175&search=Far-Hearing|Spell Link]]

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