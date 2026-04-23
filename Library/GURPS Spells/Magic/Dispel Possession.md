---
tags:
  - Spell
  - SpellsAsMagic
spellID: pNZgIdZ1pfYbxZp_y 
spellName: Dispel Possession
spellCollege: [Communication & Empathy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Spell on subject
spellDuration: '"Instant"'
spellCastingTime: '"10 sec"'
spellCost: "10"
spellMaintenance: "-"
spellPrerequisites: [Soul Rider, Possession, ]
spellPrereqText: Soul Rider, Possession
spellSource: Magic
spellReference: M49
spellLink: [[Magic.pdf#page=51&search=Dispel Possession]]
spellPoints: 1
spellTags: Communication & Empathy
spellWeapons: 
---

 [[Magic.pdf#page=51&search=Dispel Possession|Spell Link]]

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