---
tags:
  - Spell
  - SpellsAsMagic
spellID: phy0n2xoAuPYby8Hc 
spellName: Draw Together Shards
spellCollege: [None]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"5 min"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Repair, Trace, Apportation, ]
spellPrereqText: Repair, Trace, Apportation
spellSource: Alphabet Arcane
spellReference: AA9
spellLink: [[Alphabet Arcane.pdf#page=9&search=Draw Together Shards]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Alphabet Arcane.pdf#page=9&search=Draw Together Shards|Spell Link]]

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