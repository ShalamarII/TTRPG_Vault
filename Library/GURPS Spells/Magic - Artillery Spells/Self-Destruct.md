---
tags:
  - Spell
  - SpellsAsMagic
spellID: ppZmRQgWmrcDoneLe 
spellName: Self-Destruct
spellCollege: [Fire, Meta, Necromancy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 sec"'
spellCost: "12"
spellMaintenance: "undefined"
spellPrerequisites: [Explode, 10 Spell(s) from the Fire College, 10 Spell(s) from the Meta College, 10 Spell(s) from the Necromancy College, 1 Spell(s) from 10 Colleges, Magery1, ]
spellPrereqText: Explode, 10 Spell(s) from the Fire College, 10 Spell(s) from the Meta College, 10 Spell(s) from the Necromancy College, 1 Spell(s) from 10 Colleges, Magery1
spellSource: Magic - Artillery Spells
spellReference: MAS23
spellLink: [[Magic - Artillery Spells.pdf#page=23&search=Self-Destruct]]
spellPoints: 1
spellTags: Artillery, Fire, Meta, Necromancy
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=23&search=Self-Destruct|Spell Link]]

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