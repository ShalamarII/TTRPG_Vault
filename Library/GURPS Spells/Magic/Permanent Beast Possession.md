---
tags:
  - Spell
  - SpellsAsMagic
spellID: p3Ig9n5jYsL5nZoO1 
spellName: Permanent Beast Possession
spellCollege: [Animal]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"Indefinite"'
spellCastingTime: '"1 min"'
spellCost: "20"
spellMaintenance: "-"
spellPrerequisites: [Beast Possession, Magery 2, Animal 2, ]
spellPrereqText: Beast Possession, Magery 2, Animal 2
spellSource: Magic
spellReference: M32
spellLink: [[Magic.pdf#page=34&search=Permanent Beast Possession]]
spellPoints: 1
spellTags: Animal
spellWeapons: 
---

 [[Magic.pdf#page=34&search=Permanent Beast Possession|Spell Link]]

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