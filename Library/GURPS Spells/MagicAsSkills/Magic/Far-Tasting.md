---
tags:
  - Spell
  - SpellsAsMagic
spellID: pQF9xR3ABp16_D9mD 
spellName: Far-Tasting
spellCollege: [Food, Knowledge]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"3 sec"'
spellCost: "3"
spellMaintenance: "1"
spellPrerequisites: [Does not have No Taste Or Smell, Seek Food, Seek Air, Magery 1, Food 1, Knowledge 1, ]
spellPrereqText: Does not have No Taste Or Smell, Seek Food, Seek Air, Magery 1, Food 1, Knowledge 1
spellSource: Magic
spellReference: M77
spellLink: [[Magic.pdf#page=79&search=Far-Tasting]]
spellPoints: 1
spellTags: Food, Knowledge
spellWeapons: 
---

 [[Magic.pdf#page=79&search=Far-Tasting|Spell Link]]

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