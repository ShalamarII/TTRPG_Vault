---
tags:
  - Spell
  - SpellsAsMagic
spellID: pr5b_517VzzRxaiuq 
spellName: Dust to Dust
spellCollege: [Earth]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"4 sec"'
spellCost: "13"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Earth 3, Flesh To Stone, Earth To Air, ]
spellPrereqText: Magery 3, Earth 3, Flesh To Stone, Earth To Air
spellSource: Magic - Death Spells
spellReference: MDS11
spellLink: [[Magic - Death Spells.pdf#page=11&search=Dust to Dust]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=11&search=Dust to Dust|Spell Link]]

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