---
tags:
  - Spell
  - SpellsAsMagic
spellID: pmjKyekf0xJgx-5ca 
spellName: Underworld Imprisonment
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"Permanent#"'
spellCastingTime: '"3 sec"'
spellCost: "14"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Gate 3, Plane Shift Other, ]
spellPrereqText: Magery 3, Gate 3, Plane Shift Other
spellSource: Magic - Death Spells
spellReference: MDS13
spellLink: [[Magic - Death Spells.pdf#page=13&search=Underworld Imprisonment]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=13&search=Underworld Imprisonment|Spell Link]]

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