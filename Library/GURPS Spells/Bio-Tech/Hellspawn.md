---
tags:
  - Spell
  - SpellsAsMagic
spellID: pc_zxILFgecppzDJY 
spellName: Hellspawn
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"5 min"'
spellCost: "20"
spellMaintenance: "undefined"
spellPrerequisites: [Summon Demon, ]
spellPrereqText: Summon Demon
spellSource: Bio-Tech
spellReference: BT32
spellLink: [[Bio-Tech.pdf#page=32&search=Hellspawn]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Bio-Tech.pdf#page=32&search=Hellspawn|Spell Link]]

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