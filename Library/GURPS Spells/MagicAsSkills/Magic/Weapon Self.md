---
tags:
  - Spell
  - SpellsAsMagic
spellID: pS6UNI0QE1nlwjJKJ 
spellName: Weapon Self
spellCollege: [Making & Breaking]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT or effective skill for magic weapons
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "8"
spellMaintenance: "4"
spellPrerequisites: [5 Spell(s) from the Making & Breaking College, Reshape, Apportation, Magery 2, Making & Breaking 2, ]
spellPrereqText: 5 Spell(s) from the Making & Breaking College, Reshape, Apportation, Magery 2, Making & Breaking 2
spellSource: Magic
spellReference: M119
spellLink: [[Magic.pdf#page=121&search=Weapon Self]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: 
---

 [[Magic.pdf#page=121&search=Weapon Self|Spell Link]]

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