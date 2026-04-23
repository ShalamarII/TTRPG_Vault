---
tags:
  - Spell
  - SpellsAsMagic
spellID: pbwkt9ev0VlhEbaE9 
spellName: Androgyny
spellCollege: [None]
spellDifficulty: IQ/H
spellClass: Regular/R-HT
spellResisted: undefined
spellDuration: '"1 hour"'
spellCastingTime: '"2 min"'
spellCost: "7"
spellMaintenance: "5"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Pyramid 3 - 28
spellReference: PY28:14
spellLink: [[Pyramid 3 - 28.pdf#page=14&search=Androgyny]]
spellPoints: 1
spellTags: Secret
spellWeapons: 
---

 [[Pyramid 3 - 28.pdf#page=14&search=Androgyny|Spell Link]]

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