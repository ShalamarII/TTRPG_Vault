---
tags:
  - Spell
  - SpellsAsMagic
spellID: pm6PM8dRmmn3V75ua 
spellName: Summon Earth Elemental
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"30 sec"'
spellCost: "4#"
spellMaintenance: "-"
spellPrerequisites: [Summon Fire Elemental, Summon Air Elemental, 4 Spell(s) from the Earth College, 8 Spell(s) from the Earth College, Magery 1, Earth 1, ]
spellPrereqText: Summon Fire Elemental, Summon Air Elemental, 4 Spell(s) from the Earth College, 8 Spell(s) from the Earth College, Magery 1, Earth 1
spellSource: Magic
spellReference: M27
spellLink: [[Magic.pdf#page=29&search=Summon Earth Elemental]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic.pdf#page=29&search=Summon Earth Elemental|Spell Link]]

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