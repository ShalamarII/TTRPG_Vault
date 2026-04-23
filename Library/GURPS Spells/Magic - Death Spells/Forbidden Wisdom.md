---
tags:
  - Spell
  - SpellsAsMagic
spellID: pNt7uRMCFV-azi5OL 
spellName: Forbidden Wisdom
spellCollege: [Knowledge]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: IQ
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "11"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Knowledge 3, Recall, See Secrets, ]
spellPrereqText: Magery 3, Knowledge 3, Recall, See Secrets
spellSource: Magic - Death Spells
spellReference: MDS15
spellLink: [[Magic - Death Spells.pdf#page=15&search=Forbidden Wisdom]]
spellPoints: 1
spellTags: Knowledge
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=15&search=Forbidden Wisdom|Spell Link]]

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