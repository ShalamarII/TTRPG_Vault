---
tags:
  - Spell
  - SpellsAsMagic
spellID: p894dEjWV_Duvhmlt 
spellName: Body of Ice
spellCollege: [Water]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "7"
spellMaintenance: "3"
spellPrerequisites: [Magery 2, Water 2, Freeze, Body Of Water, ]
spellPrereqText: Magery 2, Water 2, Freeze, Body Of Water
spellSource: Magic
spellReference: M189
spellLink: [[Magic.pdf#page=191&search=Body of Ice]]
spellPoints: 1
spellTags: Water
spellWeapons: 
---

 [[Magic.pdf#page=191&search=Body of Ice|Spell Link]]

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