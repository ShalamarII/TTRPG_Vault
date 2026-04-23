---
tags:
  - Spell
  - SpellsAsMagic
spellID: ppH3eBEY5aIVJXgNr 
spellName: Inscribe
spellCollege: [Illusion & Creation, Making & Breaking]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: Will
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1/min 2"
spellMaintenance: "Same"
spellPrerequisites: [Simple Illusion, Copy, ]
spellPrereqText: Simple Illusion, Copy
spellSource: Magic
spellReference: M97
spellLink: [[Magic.pdf#page=99&search=Inscribe]]
spellPoints: 1
spellTags: Illusion & Creation, Making & Breaking
spellWeapons: 
---

 [[Magic.pdf#page=99&search=Inscribe|Spell Link]]

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