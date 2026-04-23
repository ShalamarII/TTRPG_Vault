---
tags:
  - Spell
  - SpellsAsMagic
spellID: p93wai-7lquOTP2zh 
spellName: Know Recipe
spellCollege: [Food, Knowledge]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: Special
spellDuration: '"1 day"'
spellCastingTime: '"15 sec"'
spellCost: "3"
spellMaintenance: "-"
spellPrerequisites: [Far-tasting, Season, ]
spellPrereqText: Far-tasting, Season
spellSource: Magic
spellReference: M78
spellLink: [[Magic.pdf#page=80&search=Know Recipe]]
spellPoints: 1
spellTags: Food, Knowledge
spellWeapons: 
---

 [[Magic.pdf#page=80&search=Know Recipe|Spell Link]]

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