---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Improved (Missile)
spellCollege: [Meta]
spellDifficulty: 
spellClass: Missile
spellResisted: 
spellDuration: '"1 minute"'
spellCastingTime: '"1 second."'
spellCost: "1-3; damage depends on the energy used in the spell. All of the energy is spent at"
spellMaintenance: ""
spellPrerequisites: [Magery 2 and the regular Missile spell of the same type.]
spellPrereqText: Magery 2 and the regular Missile spell of the same type.
spellSource: Codex Arcanum
spellReference: GOCA354
spellLink: [[Codex Arcanum.pdf#page=354&search=Improved (Missile)]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=354&search=Improved (Missile)|Spell Link]]

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