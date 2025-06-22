---
tags:
  - Spell
  - SpellsAsMagic
spellID: pelZwzxqv6R0NGYln 
spellName: Butcher
spellCollege: [Food]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Special
spellDuration: '"Instant"'
spellCastingTime: '"10 sec"'
spellCost: "Special"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Food 3, Prepare Game, ]
spellPrereqText: Magery 3, Food 3, Prepare Game
spellSource: Magic - Death Spells
spellReference: MDS12
spellLink: [[Magic - Death Spells.pdf#page=12&search=Butcher]]
spellPoints: 1
spellTags: Food
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=12&search=Butcher|Spell Link]]

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