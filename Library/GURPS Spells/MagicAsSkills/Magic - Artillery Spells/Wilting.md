---
tags:
  - Spell
  - SpellsAsMagic
spellID: pJ1IE0qOYnhU5U_Zq 
spellName: Wilting
spellCollege: [Water]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 sec/1d"'
spellCost: "2/1d"
spellMaintenance: "undefined"
spellPrerequisites: [Dehydrate, 10 Spell(s) from the Water College, Magery4, ]
spellPrereqText: Dehydrate, 10 Spell(s) from the Water College, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS28
spellLink: [[Magic - Artillery Spells.pdf#page=28&search=Wilting]]
spellPoints: 1
spellTags: Artillery, Water
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=28&search=Wilting|Spell Link]]

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