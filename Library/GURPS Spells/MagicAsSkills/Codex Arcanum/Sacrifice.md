---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Sacrifice
spellCollege: [Necromancy]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"Mana generated must be used within 1 hour after the last sacrifice."'
spellCastingTime: '"1 hour."'
spellCost: "None"
spellMaintenance: "3 to maintain"
spellPrerequisites: [6 Necromantic spells, including Steal HT]
spellPrereqText: 6 Necromantic spells, including Steal HT
spellSource: Codex Arcanum
spellReference: GOCA445
spellLink: [[Codex Arcanum.pdf#page=445&search=Sacrifice]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=445&search=Sacrifice|Spell Link]]

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