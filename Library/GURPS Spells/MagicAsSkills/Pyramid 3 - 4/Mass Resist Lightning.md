---
tags:
  - Spell
  - SpellsAsMagic
spellID: pk0ePp9ni7MQybCmI 
spellName: Mass Resist Lightning
spellCollege: [Air, Protection & Warning, Weather]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 minute"'
spellCastingTime: '"1 sec/energy point"'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Pyramid 3 - 4
spellReference: PY4:9
spellLink: [[Pyramid 3 - 4.pdf#page=9&search=Mass Resist Lightning]]
spellPoints: 1
spellTags: Air, Protection & Warning, Secret, Weather
spellWeapons: 
---

 [[Pyramid 3 - 4.pdf#page=9&search=Mass Resist Lightning|Spell Link]]

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