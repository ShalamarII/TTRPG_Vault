---
tags:
  - Spell
  - SpellsAsMagic
spellID: pxpZQBSmh1H6TOz0N 
spellName: Animate Fungus
spellCollege: [Fungus]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 Min."'
spellCastingTime: '"5 Sec."'
spellCost: "3"
spellMaintenance: "Half"
spellPrerequisites: [Fungus Control, 7 Spell(s) from the Fungus College, ]
spellPrereqText: Fungus Control, 7 Spell(s) from the Fungus College
spellSource: Magic - Plant Spells
spellReference: MPS17
spellLink: [[Magic - Plant Spells.pdf#page=17&search=Animate Fungus]]
spellPoints: 1
spellTags: Fungus
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=17&search=Animate Fungus|Spell Link]]

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