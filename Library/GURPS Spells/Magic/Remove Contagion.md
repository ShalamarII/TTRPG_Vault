---
tags:
  - Spell
  - SpellsAsMagic
spellID: pL_PMC8Oi_E51ZzWL 
spellName: Remove Contagion
spellCollege: [Healing]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"2 sec"'
spellCost: "3"
spellMaintenance: "-"
spellPrerequisites: [Decay, Clean, Cure Disease, ]
spellPrereqText: Decay, Clean, Cure Disease
spellSource: Magic
spellReference: M90
spellLink: [[Magic.pdf#page=92&search=Remove Contagion]]
spellPoints: 1
spellTags: Healing
spellWeapons: 
---

 [[Magic.pdf#page=92&search=Remove Contagion|Spell Link]]

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