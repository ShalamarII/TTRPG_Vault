---
tags:
  - Spell
  - SpellsAsMagic
spellID: pnNJkNJSfnT27v-xS 
spellName: Sanctuary
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "5"
spellMaintenance: "Same"
spellPrerequisites: [Hideaway, Teleport, ]
spellPrereqText: Hideaway, Teleport
spellSource: Magic
spellReference: M86
spellLink: [[Magic.pdf#page=88&search=Sanctuary]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=88&search=Sanctuary|Spell Link]]

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