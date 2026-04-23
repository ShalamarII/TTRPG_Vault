---
tags:
  - Spell
  - SpellsAsMagic
spellID: pyXk79vBSgSqWGi5i 
spellName: Charm
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Will
spellDuration: '"1 min"'
spellCastingTime: '"3 sec"'
spellCost: "6"
spellMaintenance: "3"
spellPrerequisites: [7 Spell(s) from the Mind Control College, Loyalty, Magery 1, Mind Control 1, ]
spellPrereqText: 7 Spell(s) from the Mind Control College, Loyalty, Magery 1, Mind Control 1
spellSource: Magic
spellReference: M139
spellLink: [[Magic.pdf#page=141&search=Charm]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=141&search=Charm|Spell Link]]

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