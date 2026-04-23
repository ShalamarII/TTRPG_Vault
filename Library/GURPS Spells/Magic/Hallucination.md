---
tags:
  - Spell
  - SpellsAsMagic
spellID: p0AEPN_FTbISX8Fxl 
spellName: Hallucination
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Will
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Madness, Suggestion, ]
spellPrereqText: Madness, Suggestion
spellSource: Magic
spellReference: M140
spellLink: [[Magic.pdf#page=142&search=Hallucination]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=142&search=Hallucination|Spell Link]]

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