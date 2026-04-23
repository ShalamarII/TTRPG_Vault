---
tags:
  - Spell
  - SpellsAsMagic
spellID: pY_issK3SBH2vnnp5 
spellName: Grave Grounding
spellCollege: [Weather]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "14"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Weather 3, Body Of Lightning, Resist Lightning, ]
spellPrereqText: Magery 3, Weather 3, Body Of Lightning, Resist Lightning
spellSource: Magic - Death Spells
spellReference: MDS22
spellLink: [[Magic - Death Spells.pdf#page=22&search=Grave Grounding]]
spellPoints: 1
spellTags: Weather
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=22&search=Grave Grounding|Spell Link]]

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