---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Control Weather
spellCollege: [Earth]
spellDifficulty: 
spellClass: Area
spellResisted: 
spellDuration: '"6 hours"'
spellCastingTime: '"10 minutes."'
spellCost: "1/20. Cost to maintain is the same. Cost doubles for each 'step' of change from the"
spellMaintenance: ""
spellPrerequisites: [Magery 2, Clouds, Rain, Windstorm, Whirlwind, Snow, Cold, at least 10 spells each]
spellPrereqText: Magery 2, Clouds, Rain, Windstorm, Whirlwind, Snow, Cold, at least 10 spells each
spellSource: Codex Arcanum
spellReference: GOCA170
spellLink: [[Codex Arcanum.pdf#page=170&search=Control Weather]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=170&search=Control Weather|Spell Link]]

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