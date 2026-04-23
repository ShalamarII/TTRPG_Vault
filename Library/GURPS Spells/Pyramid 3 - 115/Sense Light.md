---
tags:
  - Spell
  - SpellsAsMagic
spellID: p40_inVkMX09hR6lb 
spellName: Sense Light
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 hour"'
spellCastingTime: '"1 sec"'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [Light, Infravision, Sense Foes, ]
spellPrereqText: Light, Infravision, Sense Foes
spellSource: Pyramid 3 - 115
spellReference: PY115:22
spellLink: [[Pyramid 3 - 115.pdf#page=22&search=Sense Light]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Pyramid 3 - 115.pdf#page=22&search=Sense Light|Spell Link]]

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