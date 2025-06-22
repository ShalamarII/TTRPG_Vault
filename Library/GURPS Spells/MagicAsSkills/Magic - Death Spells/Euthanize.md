---
tags:
  - Spell
  - SpellsAsMagic
spellID: pYJSoVuc_RBi0P0lE 
spellName: Euthanize
spellCollege: [Healing]
spellDifficulty: IQ/VH
spellClass: Special
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 min"'
spellCost: "8"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Healing 1, Status, Spirit Empathy, ]
spellPrereqText: Magery 1, Healing 1, Status, Spirit Empathy
spellSource: Magic - Death Spells
spellReference: MDS14
spellLink: [[Magic - Death Spells.pdf#page=14&search=Euthanize]]
spellPoints: 1
spellTags: Healing
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=14&search=Euthanize|Spell Link]]

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