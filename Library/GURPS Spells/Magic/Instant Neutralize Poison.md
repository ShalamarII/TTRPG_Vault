---
tags:
  - Spell
  - SpellsAsMagic
spellID: pm__JFQa4dTynnPgY 
spellName: Instant Neutralize Poison
spellCollege: [Healing]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec"'
spellCost: "8"
spellMaintenance: "-"
spellPrerequisites: [Magery 2, Healing 2, Neutralize Poison, ]
spellPrereqText: Magery 2, Healing 2, Neutralize Poison
spellSource: Magic
spellReference: M92
spellLink: [[Magic.pdf#page=94&search=Instant Neutralize Poison]]
spellPoints: 1
spellTags: Healing
spellWeapons: 
---

 [[Magic.pdf#page=94&search=Instant Neutralize Poison|Spell Link]]

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