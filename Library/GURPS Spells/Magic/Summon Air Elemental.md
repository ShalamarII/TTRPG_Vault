---
tags:
  - Spell
  - SpellsAsMagic
spellID: pd5ruSwNpzBi0ygoB 
spellName: Summon Air Elemental
spellCollege: [Air]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"30 sec"'
spellCost: "Special"
spellMaintenance: "-"
spellPrerequisites: [Summon Fire Elemental, Summon Water Elemental, 4 Spell(s) from the Air College, 8 Spell(s) from the Air College, Magery 1, Air 1, ]
spellPrereqText: Summon Fire Elemental, Summon Water Elemental, 4 Spell(s) from the Air College, 8 Spell(s) from the Air College, Magery 1, Air 1
spellSource: Magic
spellReference: M27
spellLink: [[Magic.pdf#page=29&search=Summon Air Elemental]]
spellPoints: 1
spellTags: Air
spellWeapons: 
---

 [[Magic.pdf#page=29&search=Summon Air Elemental|Spell Link]]

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