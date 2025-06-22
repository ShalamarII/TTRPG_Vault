---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBMbrzpCX4yZANFdC 
spellName: Splat
spellCollege: [Gate, Movement]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"3 secs"'
spellCost: "5"
spellMaintenance: "undefined"
spellPrerequisites: [Create Door, Magery4, ]
spellPrereqText: Create Door, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS16
spellLink: [[Magic - Artillery Spells.pdf#page=16&search=Splat]]
spellPoints: 1
spellTags: Artillery, Gate, Movement
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=16&search=Splat|Spell Link]]

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