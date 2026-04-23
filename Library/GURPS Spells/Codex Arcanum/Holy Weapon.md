---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Holy Weapon
spellCollege: [Meta]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 turn"'
spellCastingTime: '"1 second per energy point used to cast the spell."'
spellCost: "1-3"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Clerical Power Investment, Puissance, Sharpen.]
spellPrereqText: Clerical Power Investment, Puissance, Sharpen.
spellSource: Codex Arcanum
spellReference: GOCA370
spellLink: [[Codex Arcanum.pdf#page=370&search=Holy Weapon]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=370&search=Holy Weapon|Spell Link]]

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