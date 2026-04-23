---
tags:
  - Spell
  - SpellsAsMagic
spellID: pPQw3q5Xm2FYUeZhX 
spellName: Fungus Growth
spellCollege: [Fungus]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"10 sec"'
spellCost: "3"
spellMaintenance: "2"
spellPrerequisites: [Heal Fungus, ]
spellPrereqText: Heal Fungus
spellSource: Magic - Plant Spells
spellReference: MPS17
spellLink: [[Magic - Plant Spells.pdf#page=17&search=Fungus Growth]]
spellPoints: 1
spellTags: Fungus
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=17&search=Fungus Growth|Spell Link]]

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