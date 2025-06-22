---
tags:
  - Spell
  - SpellsAsMagic
spellID: pcYPyXuaistUKmMtN 
spellName: Soul Prison
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"Permanent, unless reversed by Remove Curse before the subject dies"'
spellCastingTime: '"3 sec"'
spellCost: "12"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Necromancy 3, Banish, Soul Jar, ]
spellPrereqText: Magery 3, Necromancy 3, Banish, Soul Jar
spellSource: Magic - Death Spells
spellReference: MDS18
spellLink: [[Magic - Death Spells.pdf#page=18&search=Soul Prison]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=18&search=Soul Prison|Spell Link]]

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