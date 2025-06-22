---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Summon Nature Spirit
spellCollege: [Plant]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"Entirely up to the spirit. It might quickly become bored and leave or it might remain for"'
spellCastingTime: '"5 minutes"'
spellCost: "Equal to the spirit's ST + IQ. If the caster is not certain what spirit will be summoned"
spellMaintenance: "same to maintain"
spellPrerequisites: [Magery, 10 Plant Spells]
spellPrereqText: Magery, 10 Plant Spells
spellSource: Codex Arcanum
spellReference: GOCA475
spellLink: [[Codex Arcanum.pdf#page=475&search=Summon Nature Spirit]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=475&search=Summon Nature Spirit|Spell Link]]

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