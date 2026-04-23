---
tags:
  - Spell
  - SpellsAsMagic
spellID: pV6QCS1GEiBDamWL5 
spellName: Control Air Elemental
spellCollege: [Air]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Higher of ST or Will
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "Special"
spellMaintenance: "Special"
spellPrerequisites: [Summon Air Elemental, ]
spellPrereqText: Summon Air Elemental
spellSource: Magic
spellReference: M28
spellLink: [[Magic.pdf#page=30&search=Control Air Elemental]]
spellPoints: 1
spellTags: Air
spellWeapons: 
---

 [[Magic.pdf#page=30&search=Control Air Elemental|Spell Link]]

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