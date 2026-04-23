---
tags:
  - Spell
  - SpellsAsMagic
spellID: ppN_HXA3md-WBHeH_ 
spellName: Mass Daze
spellCollege: [Mind Control]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"sec=cost"'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [Daze, at least 13 IQ, ]
spellPrereqText: Daze, at least 13 IQ
spellSource: Magic
spellReference: M137
spellLink: [[Magic.pdf#page=139&search=Mass Daze]]
spellPoints: 1
spellTags: Mind Control
spellWeapons: 
---

 [[Magic.pdf#page=139&search=Mass Daze|Spell Link]]

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