---
tags:
  - Spell
  - SpellsAsMagic
spellID: pxrRD2urlw_y3_itD 
spellName: Mouth-Goes-Away
spellCollege: [None]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 day"'
spellCastingTime: '"10 min"'
spellCost: "12"
spellMaintenance: "2"
spellPrerequisites: [Magery1, Alter Visage, 4 Spell(s) from the Body Control College, ]
spellPrereqText: Magery1, Alter Visage, 4 Spell(s) from the Body Control College
spellSource: Alphabet Arcane
spellReference: AA17
spellLink: [[Alphabet Arcane.pdf#page=17&search=Mouth-Goes-Away]]
spellPoints: 1
spellTags: Lidless Eye
spellWeapons: 
---

 [[Alphabet Arcane.pdf#page=17&search=Mouth-Goes-Away|Spell Link]]

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