---
tags:
  - Spell
  - SpellsAsMagic
spellID: p-R3E-D7n5Hrj7peN 
spellName: Pestilence
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"30 sec"'
spellCost: "6"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Necromancy 1, Steal Vitality, Decay, ]
spellPrereqText: Magery 1, Necromancy 1, Steal Vitality, Decay
spellSource: Magic
spellReference: M154
spellLink: [[Magic.pdf#page=156&search=Pestilence]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=156&search=Pestilence|Spell Link]]

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