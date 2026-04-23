---
tags:
  - Spell
  - SpellsAsMagic
spellID: pezle6w6C6rU3LSiB 
spellName: Corpulence
spellCollege: [Body Control]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"10 min"'
spellCastingTime: '"3 sec"'
spellCost: "6"
spellMaintenance: "6"
spellPrerequisites: [Magery 2, Body Control 2, Create Earth, Create Water, 3 Spell(s) from the Body Control College, Alter Body, ]
spellPrereqText: Magery 2, Body Control 2, Create Earth, Create Water, 3 Spell(s) from the Body Control College, Alter Body
spellSource: Magic
spellReference: M43
spellLink: [[Magic.pdf#page=45&search=Corpulence]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=45&search=Corpulence|Spell Link]]

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