---
tags:
  - Spell
  - SpellsAsMagic
spellID: pGkZDyIsKkeHNo5GB 
spellName: Lesser Geas
spellCollege: [Mind Control]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"Until fulfilled"'
spellCastingTime: '"30 sec"'
spellCost: "12"
spellMaintenance: "-"
spellPrerequisites: [Command, 10 Spell(s) from the Mind Control College, Magery 2, Mind Control 2, ]
spellPrereqText: Command, 10 Spell(s) from the Mind Control College, Magery 2, Mind Control 2
spellSource: Magic
spellReference: M140
spellLink: [[Magic.pdf#page=142&search=Lesser Geas]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=142&search=Lesser Geas|Spell Link]]

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