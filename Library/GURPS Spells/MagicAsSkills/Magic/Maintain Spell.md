---
tags:
  - Spell
  - SpellsAsMagic
spellID: pdSB4X7fLQhmkSaYo 
spellName: Maintain Spell
spellCollege: [Meta]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"2 sec"'
spellCost: "maint cost of subject spell"
spellMaintenance: "-"
spellPrerequisites: [Link, ]
spellPrereqText: Link
spellSource: Magic
spellReference: M128
spellLink: [[Magic.pdf#page=130&search=Maintain Spell]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=130&search=Maintain Spell|Spell Link]]

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