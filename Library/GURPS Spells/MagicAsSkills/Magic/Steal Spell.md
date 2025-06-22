---
tags:
  - Spell
  - SpellsAsMagic
spellID: pJ8IhjdYS4hVCrLq- 
spellName: Steal Spell
spellCollege: [Meta]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Subject spell
spellDuration: '"Permanent"'
spellCastingTime: '"sec=cost"'
spellCost: "maint cost of stolen spell"
spellMaintenance: "-"
spellPrerequisites: [Lend Spell, Great Ward, ]
spellPrereqText: Lend Spell, Great Ward
spellSource: Magic
spellReference: M127
spellLink: [[Magic.pdf#page=129&search=Steal Spell]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=129&search=Steal Spell|Spell Link]]

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