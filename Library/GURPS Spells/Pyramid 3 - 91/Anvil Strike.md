---
tags:
  - Spell
  - SpellsAsMagic
spellID: p6wZI3fJ8IG5-ob7U 
spellName: Anvil Strike
spellCollege: [Metal]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"varies"'
spellCost: "varies"
spellMaintenance: "undefined"
spellPrerequisites: [Magery 3, Metal 3, Teleport, Rain Of Shards, ]
spellPrereqText: Magery 3, Metal 3, Teleport, Rain Of Shards
spellSource: Pyramid 3 - 91
spellReference: PY91:23
spellLink: [[Pyramid 3 - 91.pdf#page=23&search=Anvil Strike]]
spellPoints: 1
spellTags: Metal
spellWeapons: 
---

 [[Pyramid 3 - 91.pdf#page=23&search=Anvil Strike|Spell Link]]

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