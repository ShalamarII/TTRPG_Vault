---
tags:
  - Spell
  - SpellsAsMagic
spellID: pzfE3xGL_tWPWdBzH 
spellName: Resurrection
spellCollege: [Healing, Necromancy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"2 Hours"'
spellCost: "300"
spellMaintenance: "-"
spellPrerequisites: [Instant Regeneration, Summon Spirit, ]
spellPrereqText: Instant Regeneration, Summon Spirit
spellSource: Magic
spellReference: M94
spellLink: [[Magic.pdf#page=96&search=Resurrection]]
spellPoints: 1
spellTags: Healing, Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=96&search=Resurrection|Spell Link]]

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