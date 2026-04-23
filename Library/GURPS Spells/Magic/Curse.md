---
tags:
  - Spell
  - SpellsAsMagic
spellID: pJx_KzKO54T4kChDe 
spellName: Curse
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"2/4/6 sec"'
spellCost: "3/10/20"
spellMaintenance: "-"
spellPrerequisites: [1 Spell(s) from 10 Colleges, Magery 3, Meta 3, ]
spellPrereqText: 1 Spell(s) from 10 Colleges, Magery 3, Meta 3
spellSource: Magic
spellReference: M129
spellLink: [[Magic.pdf#page=131&search=Curse]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=131&search=Curse|Spell Link]]

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