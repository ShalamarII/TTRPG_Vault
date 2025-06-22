---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Pass Spell
spellCollege: [Meta]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"As the Duration of the other spell"'
spellCastingTime: '"3 seconds"'
spellCost: "1 per hex (or if cast on a spell without an area effect"
spellMaintenance: "2 points), same to maintain"
spellPrerequisites: [Link]
spellPrereqText: Link
spellSource: Codex Arcanum
spellReference: GOCA361
spellLink: [[Codex Arcanum.pdf#page=361&search=Pass Spell]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=361&search=Pass Spell|Spell Link]]

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