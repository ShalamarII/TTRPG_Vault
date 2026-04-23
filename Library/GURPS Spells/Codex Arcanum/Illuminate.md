---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Illuminate
spellCollege: [Making and Breaking]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"Permanent."'
spellCastingTime: '"5 seconds plus 30 minutes for the spell to finish."'
spellCost: "6."
spellMaintenance: ""
spellPrerequisites: [Paint.]
spellPrereqText: Paint.
spellSource: Codex Arcanum
spellReference: GOCA328
spellLink: [[Codex Arcanum.pdf#page=328&search=Illuminate]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=328&search=Illuminate|Spell Link]]

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