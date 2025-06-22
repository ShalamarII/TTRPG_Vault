---
tags:
  - Spell
  - SpellsAsMagic
spellID: p8wk6vHeT2_qD4Igk 
spellName: Shadow-Slay
spellCollege: [Light & Darkness]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT or Will
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "14"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Light & Darkness 3, Body Of Shadow, Remove Shadow, ]
spellPrereqText: Magery 3, Light & Darkness 3, Body Of Shadow, Remove Shadow
spellSource: Magic - Death Spells
spellReference: MDS16
spellLink: [[Magic - Death Spells.pdf#page=16&search=Shadow-Slay]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=16&search=Shadow-Slay|Spell Link]]

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