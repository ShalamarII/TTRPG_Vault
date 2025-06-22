---
tags:
  - Spell
  - SpellsAsMagic
spellID: phxgPJOY7HtvHEN7U 
spellName: Dread Curse
spellCollege: [Meta]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"Lasting, until the subject fails a dice roll or is saved by Remove Curse."'
spellCastingTime: '"4 sec"'
spellCost: "10"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Meta 3, Curse, ]
spellPrereqText: Magery 3, Meta 3, Curse
spellSource: Magic - Death Spells
spellReference: MDS17
spellLink: [[Magic - Death Spells.pdf#page=17&search=Dread Curse]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=17&search=Dread Curse|Spell Link]]

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