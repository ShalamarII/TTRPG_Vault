---
tags:
  - Spell
  - SpellsAsMagic
spellID: pg3OfZRf-NhdOajSO 
spellName: Compel Lie
spellCollege: [Communication & Empathy, Mind Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Will
spellDuration: '"5 min"'
spellCastingTime: '"1 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Emotion Control, ]
spellPrereqText: Emotion Control
spellSource: Magic
spellReference: M137
spellLink: [[Magic.pdf#page=139&search=Compel Lie]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=139&search=Compel Lie|Spell Link]]

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