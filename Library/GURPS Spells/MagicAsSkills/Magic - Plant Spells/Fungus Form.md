---
tags:
  - Spell
  - SpellsAsMagic
spellID: pMHNdIJdklg1OUsjq 
spellName: Fungus Form
spellCollege: [Fungus]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"1 hour"'
spellCastingTime: '"1 sec"'
spellCost: "5"
spellMaintenance: "2"
spellPrerequisites: [6 Spell(s) from the Fungus College, Magery 1, Fungus 1, ]
spellPrereqText: 6 Spell(s) from the Fungus College, Magery 1, Fungus 1
spellSource: Magic - Plant Spells
spellReference: MPS17
spellLink: [[Magic - Plant Spells.pdf#page=17&search=Fungus Form]]
spellPoints: 1
spellTags: Fungus
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=17&search=Fungus Form|Spell Link]]

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