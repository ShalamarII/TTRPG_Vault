---
tags:
  - Spell
  - SpellsAsMagic
spellID: p5fFbfj3yx0UNMqGc 
spellName: Great Deflect Energy
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "undefined"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Pyramid 3 - 4
spellReference: PY4:9
spellLink: [[Pyramid 3 - 4.pdf#page=9&search=Great Deflect Energy]]
spellPoints: 1
spellTags: Fire, Secret
spellWeapons: 
---

 [[Pyramid 3 - 4.pdf#page=9&search=Great Deflect Energy|Spell Link]]

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