---
tags:
  - Spell
  - SpellsAsMagic
spellID: pYtdUiJNHph5N0N3t 
spellName: Heart of Stone
spellCollege: [Earth]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"3 sec"'
spellCost: "13"
spellMaintenance: "-"
spellPrerequisites: [Partial Petrification, Magery 33, ]
spellPrereqText: Partial Petrification, Magery 33
spellSource: Magic - Death Spells
spellReference: MDS11
spellLink: [[Magic - Death Spells.pdf#page=11&search=Heart of Stone]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=11&search=Heart of Stone|Spell Link]]

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