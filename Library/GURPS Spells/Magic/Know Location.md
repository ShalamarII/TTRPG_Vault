---
tags:
  - Spell
  - SpellsAsMagic
spellID: p_97_Ma29Src28Ghg 
spellName: Know Location
spellCollege: [Knowledge]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"10 sec"'
spellCost: "2"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Knowledge 1, Tell Position, ]
spellPrereqText: Magery 1, Knowledge 1, Tell Position
spellSource: Magic
spellReference: M103
spellLink: [[Magic.pdf#page=105&search=Know Location]]
spellPoints: 1
spellTags: Knowledge
spellWeapons: 
---

 [[Magic.pdf#page=105&search=Know Location|Spell Link]]

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