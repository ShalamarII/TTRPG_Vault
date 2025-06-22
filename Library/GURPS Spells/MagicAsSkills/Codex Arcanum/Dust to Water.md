---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Dust to Water
spellCollege: [Water]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '""'
spellCost: "3 per 20 lbs. of material affected."
spellMaintenance: ""
spellPrerequisites: [Earth to Air, Create Water]
spellPrereqText: Earth to Air, Create Water
spellSource: Codex Arcanum
spellReference: GOCA217
spellLink: [[Codex Arcanum.pdf#page=217&search=Dust to Water]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=217&search=Dust to Water|Spell Link]]

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