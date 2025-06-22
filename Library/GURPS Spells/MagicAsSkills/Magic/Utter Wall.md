---
tags:
  - Spell
  - SpellsAsMagic
spellID: phZWQCPdZNAECegHn 
spellName: Utter Wall
spellCollege: [Protection & Warning]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Intruding spells
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "4/yd"
spellMaintenance: "Same"
spellPrerequisites: [Utter Dome, Spell Wall, ]
spellPrereqText: Utter Dome, Spell Wall
spellSource: Magic
spellReference: M170
spellLink: [[Magic.pdf#page=172&search=Utter Wall]]
spellPoints: 1
spellTags: Protection & Warning
spellWeapons: 
---

 [[Magic.pdf#page=172&search=Utter Wall|Spell Link]]

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