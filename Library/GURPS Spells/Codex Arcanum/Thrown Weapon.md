---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Thrown Weapon
spellCollege: [Movement]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"10 seconds"'
spellCastingTime: '"10 seconds to cast, 3 to 'program' the ‘Servant after it is created."'
spellCost: "2 points"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Apportation]
spellPrereqText: Apportation
spellSource: Codex Arcanum
spellReference: GOCA419
spellLink: [[Codex Arcanum.pdf#page=419&search=Thrown Weapon]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=419&search=Thrown Weapon|Spell Link]]

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