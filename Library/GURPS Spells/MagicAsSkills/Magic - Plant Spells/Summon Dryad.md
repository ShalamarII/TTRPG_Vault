---
tags:
  - Spell
  - SpellsAsMagic
spellID: pK4P7k-mKzUf20CDa 
spellName: Summon Dryad
spellCollege: [Air, Plant]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"30 sec"'
spellCost: "23"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Air 1, Plant 1, 7 Spell(s) from the Plant College, Sense Spirit, ]
spellPrereqText: Magery 1, Air 1, Plant 1, 7 Spell(s) from the Plant College, Sense Spirit
spellSource: Magic - Plant Spells
spellReference: MPS13
spellLink: [[Magic - Plant Spells.pdf#page=13&search=Summon Dryad]]
spellPoints: 1
spellTags: Air, Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=13&search=Summon Dryad|Spell Link]]

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