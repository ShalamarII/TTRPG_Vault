---
tags:
  - Spell
  - SpellsAsMagic
spellID: pcgu26PrnpwBZybBM 
spellName: Scents of the Past
spellCollege: [Food, Knowledge]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"10 sec"'
spellCost: "Varies"
spellMaintenance: "Same"
spellPrerequisites: [Magery 2, Food 2, Knowledge 2, History, Odor, ]
spellPrereqText: Magery 2, Food 2, Knowledge 2, History, Odor
spellSource: Magic
spellReference: M107
spellLink: [[Magic.pdf#page=109&search=Scents of the Past]]
spellPoints: 1
spellTags: Food, Knowledge
spellWeapons: 
---

 [[Magic.pdf#page=109&search=Scents of the Past|Spell Link]]

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