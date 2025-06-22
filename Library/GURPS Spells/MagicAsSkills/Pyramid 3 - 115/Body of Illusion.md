---
tags:
  - Spell
  - SpellsAsMagic
spellID: ppb2QupZEWIUZX_tj 
spellName: Body of Illusion
spellCollege: [Illusion & Creation]
spellDifficulty: IQ/H
spellClass: Regular/R-HT
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "6"
spellMaintenance: "3"
spellPrerequisites: [at least 15 IQ, Control Illusion, Magery 3, Illusion & Creation 3, ]
spellPrereqText: at least 15 IQ, Control Illusion, Magery 3, Illusion & Creation 3
spellSource: Pyramid 3 - 115
spellReference: PY115:21
spellLink: [[Pyramid 3 - 115.pdf#page=21&search=Body of Illusion]]
spellPoints: 1
spellTags: Illusion & Creation
spellWeapons: 
---

 [[Pyramid 3 - 115.pdf#page=21&search=Body of Illusion|Spell Link]]

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