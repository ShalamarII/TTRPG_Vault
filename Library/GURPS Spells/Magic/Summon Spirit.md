---
tags:
  - Spell
  - SpellsAsMagic
spellID: p7pOzQTzD6s_Giccy 
spellName: Summon Spirit
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: Spirit's Will
spellDuration: '"1 min"'
spellCastingTime: '"5 min"'
spellCost: "20"
spellMaintenance: "10"
spellPrerequisites: [Death Vision, Magery 2, Necromancy 2, ]
spellPrereqText: Death Vision, Magery 2, Necromancy 2
spellSource: Magic
spellReference: M150
spellLink: [[Magic.pdf#page=152&search=Summon Spirit]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=152&search=Summon Spirit|Spell Link]]

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