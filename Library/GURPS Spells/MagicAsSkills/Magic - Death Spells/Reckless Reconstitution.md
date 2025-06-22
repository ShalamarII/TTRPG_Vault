---
tags:
  - Spell
  - SpellsAsMagic
spellID: pYvrX9rSoYHWmDvzf 
spellName: Reckless Reconstitution
spellCollege: [Technological]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"12 sec"'
spellCost: "12"
spellMaintenance: "-"
spellPrerequisites: [Rebuild, ]
spellPrereqText: Rebuild
spellSource: Magic - Death Spells
spellReference: MDS21
spellLink: [[Magic - Death Spells.pdf#page=21&search=Reckless Reconstitution]]
spellPoints: 1
spellTags: Technological
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=21&search=Reckless Reconstitution|Spell Link]]

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