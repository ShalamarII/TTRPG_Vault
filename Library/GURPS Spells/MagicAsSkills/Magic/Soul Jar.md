---
tags:
  - Spell
  - SpellsAsMagic
spellID: pcITIMT7r0StU7qR4 
spellName: Soul Jar
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 min"'
spellCost: "8"
spellMaintenance: "-"
spellPrerequisites: [1 Spell(s) from the Necromancy College, Steal Vitality, Magery 1, Necromancy 1, ]
spellPrereqText: 1 Spell(s) from the Necromancy College, Steal Vitality, Magery 1, Necromancy 1
spellSource: Magic
spellReference: M154
spellLink: [[Magic.pdf#page=156&search=Soul Jar]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=156&search=Soul Jar|Spell Link]]

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