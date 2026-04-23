---
tags:
  - Spell
  - SpellsAsMagic
spellID: p5yrai7SjivViN527 
spellName: Death
spellCollege: [Body Control]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"3 sec"'
spellCost: "12"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Body Control 3, Deathtouch, Choke, ]
spellPrereqText: Magery 3, Body Control 3, Deathtouch, Choke
spellSource: Magic - Death Spells
spellReference: MDS10
spellLink: [[Magic - Death Spells.pdf#page=10&search=Death]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=10&search=Death|Spell Link]]

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