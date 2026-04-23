---
tags:
  - Spell
  - SpellsAsMagic
spellID: pnUN1YMx6fFXlqi0- 
spellName: Alter Visage
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 hr"'
spellCastingTime: '"1 min"'
spellCost: "4"
spellMaintenance: "3"
spellPrerequisites: [Shapeshifting, Perfect Illusion, 8 Spell(s) from the Body Control College, ]
spellPrereqText: Shapeshifting, Perfect Illusion, 8 Spell(s) from the Body Control College
spellSource: Magic
spellReference: M41
spellLink: [[Magic.pdf#page=43&search=Alter Visage]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=43&search=Alter Visage|Spell Link]]

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