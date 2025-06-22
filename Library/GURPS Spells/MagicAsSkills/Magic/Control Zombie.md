---
tags:
  - Spell
  - SpellsAsMagic
spellID: p7LvBC5VPsCJm60Hq 
spellName: Control Zombie
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Zombie spell
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "undefined"
spellPrerequisites: [Zombie, ]
spellPrereqText: Zombie
spellSource: Magic
spellReference: M152
spellLink: [[Magic.pdf#page=154&search=Control Zombie]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=154&search=Control Zombie|Spell Link]]

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