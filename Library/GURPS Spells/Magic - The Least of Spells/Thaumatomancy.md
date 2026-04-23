---
tags:
  - Spell
  - SpellsAsMagic
spellID: pmpv3D1ARIZ-gplSe 
spellName: Thaumatomancy
spellCollege: [Knowledge, Meta]
spellDifficulty: IQ/A
spellClass: Information
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 hr"'
spellCost: "10"
spellMaintenance: "-"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS12
spellLink: [[Magic - The Least of Spells.pdf#page=12&search=Thaumatomancy]]
spellPoints: 1
spellTags: Knowledge, Meta
spellWeapons: 
---

 [[Magic - The Least of Spells.pdf#page=12&search=Thaumatomancy|Spell Link]]

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