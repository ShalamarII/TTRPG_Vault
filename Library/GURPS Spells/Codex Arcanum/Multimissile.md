---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Multimissile
spellCollege: [Earth]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 seconds"'
spellCastingTime: '"1 second per point of Base Cost."'
spellCost: "1 per extra missile or per 2d6 damage to a maximum of 5 points of energy"
spellMaintenance: ""
spellPrerequisites: [Stone Missile]
spellPrereqText: Stone Missile
spellSource: Codex Arcanum
spellReference: GOCA184
spellLink: [[Codex Arcanum.pdf#page=184&search=Multimissile]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=184&search=Multimissile|Spell Link]]

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