---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Steal Dexterity
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"See Above."'
spellCastingTime: '""'
spellCost: "None for the Caster! For every 3 points of DX taken from the subject"
spellMaintenance: ""
spellPrerequisites: [Steal Strength]
spellPrereqText: Steal Strength
spellSource: Codex Arcanum
spellReference: GOCA448
spellLink: [[Codex Arcanum.pdf#page=448&search=Steal Dexterity]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=448&search=Steal Dexterity|Spell Link]]

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