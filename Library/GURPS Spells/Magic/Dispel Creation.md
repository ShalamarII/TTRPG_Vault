---
tags:
  - Spell
  - SpellsAsMagic
spellID: pE3xPcg6j1X46z3d- 
spellName: Dispel Creation
spellCollege: [Illusion & Creation]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Subject spell
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1 or 3"
spellMaintenance: "-"
spellPrerequisites: [Control Creation, ]
spellPrereqText: Control Creation
spellSource: Magic
spellReference: M99
spellLink: [[Magic.pdf#page=101&search=Dispel Creation]]
spellPoints: 1
spellTags: Illusion & Creation
spellWeapons: 
---

 [[Magic.pdf#page=101&search=Dispel Creation|Spell Link]]

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