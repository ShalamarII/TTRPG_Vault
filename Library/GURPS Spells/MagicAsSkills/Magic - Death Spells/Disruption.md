---
tags:
  - Spell
  - SpellsAsMagic
spellID: pRT6I857jTSRlfGqQ 
spellName: Disruption
spellCollege: [Movement]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"3 sec"'
spellCost: "12-18"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Movement 3, Undo, Manipulate, 10 Spell(s) from the Movement College, ]
spellPrereqText: Magery 3, Movement 3, Undo, Manipulate, 10 Spell(s) from the Movement College
spellSource: Magic - Death Spells
spellReference: MDS17
spellLink: [[Magic - Death Spells.pdf#page=17&search=Disruption]]
spellPoints: 1
spellTags: Movement
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=17&search=Disruption|Spell Link]]

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