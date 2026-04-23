---
tags:
  - Spell
  - SpellsAsMagic
spellID: pwb8mP-cVjSVUhawp 
spellName: Stone to Earth
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec"'
spellCost: "6 per 25 cu ft"
spellMaintenance: "-"
spellPrerequisites: [4 Spell(s) from the Earth College, Earth To Stone, ]
spellPrereqText: 4 Spell(s) from the Earth College, Earth To Stone
spellSource: Magic
spellReference: M51
spellLink: [[Magic.pdf#page=53&search=Stone to Earth]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic.pdf#page=53&search=Stone to Earth|Spell Link]]

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