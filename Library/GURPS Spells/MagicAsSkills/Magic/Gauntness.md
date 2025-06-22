---
tags:
  - Spell
  - SpellsAsMagic
spellID: pzENWuPYmqrDzrISH 
spellName: Gauntness
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"10 min"'
spellCastingTime: '"3 sec"'
spellCost: "6"
spellMaintenance: "6"
spellPrerequisites: [Earth To Air, Destroy Water, 3 Spell(s) from the Body Control College, Magery 2, Body Control 2, Hunger, ]
spellPrereqText: Earth To Air, Destroy Water, 3 Spell(s) from the Body Control College, Magery 2, Body Control 2, Hunger
spellSource: Magic
spellReference: M43
spellLink: [[Magic.pdf#page=45&search=Gauntness]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=45&search=Gauntness|Spell Link]]

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