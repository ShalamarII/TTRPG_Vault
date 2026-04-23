---
tags:
  - Spell
  - SpellsAsMagic
spellID: pLmqQKLNrElEAcpJv 
spellName: Wail of the Banshee
spellCollege: [Sound]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Sound 3, Message, 10 Spell(s) from the Sound College, ]
spellPrereqText: Magery 3, Sound 3, Message, 10 Spell(s) from the Sound College
spellSource: Magic - Death Spells
spellReference: MDS20
spellLink: [[Magic - Death Spells.pdf#page=20&search=Wail of the Banshee]]
spellPoints: 1
spellTags: Sound
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=20&search=Wail of the Banshee|Spell Link]]

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