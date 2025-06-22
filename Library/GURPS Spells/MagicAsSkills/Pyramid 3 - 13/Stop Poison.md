---
tags:
  - Spell
  - SpellsAsMagic
spellID: pTf-8ko61_lIhaXAI 
spellName: Stop Poison
spellCollege: [Healing]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 week"'
spellCastingTime: '"1 min"'
spellCost: "6, plus 2 per additional week of duration"
spellMaintenance: "undefined"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Pyramid 3 - 13
spellReference: PY13:27
spellLink: [[Pyramid 3 - 13.pdf#page=27&search=Stop Poison]]
spellPoints: 1
spellTags: Healing
spellWeapons: 
---

 [[Pyramid 3 - 13.pdf#page=27&search=Stop Poison|Spell Link]]

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