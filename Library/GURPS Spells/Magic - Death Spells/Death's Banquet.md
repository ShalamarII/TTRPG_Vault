---
tags:
  - Spell
  - SpellsAsMagic
spellID: p7Gjh_AJUlTzbe1nb 
spellName: Death's Banquet
spellCollege: [Food]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Special
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "3-19"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Food 3, Poison Food, Essential Food, ]
spellPrereqText: Magery 3, Food 3, Poison Food, Essential Food
spellSource: Magic - Death Spells
spellReference: MDS13
spellLink: [[Magic - Death Spells.pdf#page=13&search=Death's Banquet]]
spellPoints: 1
spellTags: Food
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=13&search=Death's Banquet|Spell Link]]

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