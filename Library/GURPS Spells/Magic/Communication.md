---
tags:
  - Spell
  - SpellsAsMagic
spellID: pmA_VrrPustT3wNsR 
spellName: Communication
spellCollege: [Communication & Empathy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"4 sec"'
spellCost: "4"
spellMaintenance: "4"
spellPrerequisites: [Wizard Eye, Far-hearing, Voices, Simple Illusion, ]
spellPrereqText: Wizard Eye, Far-hearing, Voices, Simple Illusion
spellSource: Magic
spellReference: M48
spellLink: [[Magic.pdf#page=50&search=Communication]]
spellPoints: 1
spellTags: Communication & Empathy
spellWeapons: 
---

 [[Magic.pdf#page=50&search=Communication|Spell Link]]

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