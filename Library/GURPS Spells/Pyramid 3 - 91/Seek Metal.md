---
tags:
  - Spell
  - SpellsAsMagic
spellID: pngpFDD1sjf_abtS9 
spellName: Seek Metal
spellCollege: [Knowledge, Metal]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"10 sec"'
spellCost: "3"
spellMaintenance: "-"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Pyramid 3 - 91
spellReference: PY91:27
spellLink: [[Pyramid 3 - 91.pdf#page=27&search=Seek Metal]]
spellPoints: 1
spellTags: Knowledge, Metal
spellWeapons: 
---

 [[Pyramid 3 - 91.pdf#page=27&search=Seek Metal|Spell Link]]

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