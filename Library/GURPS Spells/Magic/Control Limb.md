---
tags:
  - Spell
  - SpellsAsMagic
spellID: pFIpmnaXnSGljjrXg 
spellName: Control Limb
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Will
spellDuration: '"5 sec"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "3"
spellPrerequisites: [4 Spell(s) from the Body Control College, Spasm, Magery 1, Body Control 1, ]
spellPrereqText: 4 Spell(s) from the Body Control College, Spasm, Magery 1, Body Control 1
spellSource: Magic
spellReference: M40
spellLink: [[Magic.pdf#page=42&search=Control Limb]]
spellPoints: 1
spellTags: Body Control
spellWeapons: 
---

 [[Magic.pdf#page=42&search=Control Limb|Spell Link]]

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