---
tags:
  - Spell
  - SpellsAsMagic
spellID: pJbHNnlJU8K8XuQ_8 
spellName: Mark of Thieves
spellCollege: [None]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Will
spellDuration: '"1 week"'
spellCastingTime: '"5 min"'
spellCost: "4"
spellMaintenance: "undefined"
spellPrerequisites: [Magery1, Pestilence, ]
spellPrereqText: Magery1, Pestilence
spellSource: Alphabet Arcane
spellReference: AA17
spellLink: [[Alphabet Arcane.pdf#page=17&search=Mark of Thieves]]
spellPoints: 1
spellTags: Lidless Eye
spellWeapons: 
---

 [[Alphabet Arcane.pdf#page=17&search=Mark of Thieves|Spell Link]]

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