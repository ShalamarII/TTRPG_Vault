---
tags:
  - Spell
  - SpellsAsMagic
spellID: pt9C-24TMzGRcdH0S 
spellName: Slow Healing
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 day"'
spellCastingTime: '"30 sec"'
spellCost: "1-5"
spellMaintenance: "Same"
spellPrerequisites: [Frailty, Magery 1, Necromancy 1, Steal Vitality, ]
spellPrereqText: Frailty, Magery 1, Necromancy 1, Steal Vitality
spellSource: Magic
spellReference: M153
spellLink: [[Magic.pdf#page=155&search=Slow Healing]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=155&search=Slow Healing|Spell Link]]

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