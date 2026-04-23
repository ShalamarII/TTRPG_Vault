---
tags:
  - Spell
  - SpellsAsMagic
spellID: pjjDhO-NpkBNzg9fC 
spellName: Fatal Frequency
spellCollege: [Sound]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"3 sec"'
spellCost: "7-14"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Sound 3, Concussion, Sound Jet, ]
spellPrereqText: Magery 3, Sound 3, Concussion, Sound Jet
spellSource: Magic - Death Spells
spellReference: MDS20
spellLink: [[Magic - Death Spells.pdf#page=20&search=Fatal Frequency]]
spellPoints: 1
spellTags: Sound
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=20&search=Fatal Frequency|Spell Link]]

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