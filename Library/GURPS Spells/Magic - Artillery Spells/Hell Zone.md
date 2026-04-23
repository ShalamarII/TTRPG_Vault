---
tags:
  - Spell
  - SpellsAsMagic
spellID: pZ1l9Its8oU_9J0Jp 
spellName: Hell Zone
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"10 secs"'
spellCastingTime: '"1/2 base cost"'
spellCost: "10"
spellMaintenance: "Half"
spellPrerequisites: [Beacon, Planar Summons, Magery4, ]
spellPrereqText: Beacon, Planar Summons, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS16
spellLink: [[Magic - Artillery Spells.pdf#page=16&search=Hell Zone]]
spellPoints: 1
spellTags: Artillery, Gate
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=16&search=Hell Zone|Spell Link]]

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