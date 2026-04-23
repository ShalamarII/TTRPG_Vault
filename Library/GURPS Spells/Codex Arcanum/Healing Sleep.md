---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Healing Sleep
spellCollege: [Healing]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 to 12 hours."'
spellCastingTime: '"1 minute, plus 1 hour of concentration per point of HT to be healed."'
spellCost: "3"
spellMaintenance: ""
spellPrerequisites: [Diagnosis (skill or spell), Restorative Sleep.]
spellPrereqText: Diagnosis (skill or spell), Restorative Sleep.
spellSource: Codex Arcanum
spellReference: GOCA241
spellLink: [[Codex Arcanum.pdf#page=241&search=Healing Sleep]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=241&search=Healing Sleep|Spell Link]]

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