---
tags:
  - Spell
  - SpellsAsMagic
spellID: puZIGhwBAypkzi6_P 
spellName: Suicide
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: -
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "Special"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, ]
spellPrereqText: Magery 1
spellSource: Magic - Death Spells
spellReference: MDS19
spellLink: [[Magic - Death Spells.pdf#page=19&search=Suicide]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=19&search=Suicide|Spell Link]]

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