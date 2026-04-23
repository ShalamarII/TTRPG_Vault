---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Rechargeu005CTL
spellCollege: [Electricity]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '"5 seconds per point of fatigue given to the cell."'
spellCost: "2 for each point of fatigue given to the spell. Can be combined with Draw Power to"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Lend Power and Conduct Power]
spellPrereqText: Lend Power and Conduct Power
spellSource: Codex Arcanum
spellReference: GOCA9
spellLink: [[Codex Arcanum.pdf#page=9&search=Rechargeu005CTL]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=9&search=Rechargeu005CTL|Spell Link]]

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