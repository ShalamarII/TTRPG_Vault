---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Chant
spellCollege: [Meta]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"Indefinite (see above)"'
spellCastingTime: '"1 minute, may be continued indefinitely."'
spellCost: "None. Energy gained from this spell can only be used to maintain spells"
spellMaintenance: ""
spellPrerequisites: [Magery, Regain ST]
spellPrereqText: Magery, Regain ST
spellSource: Codex Arcanum
spellReference: GOCA346
spellLink: [[Codex Arcanum.pdf#page=346&search=Chant]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=346&search=Chant|Spell Link]]

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