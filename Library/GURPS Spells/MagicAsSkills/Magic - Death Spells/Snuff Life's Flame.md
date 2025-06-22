---
tags:
  - Spell
  - SpellsAsMagic
spellID: p1iAT27cT-mme-ad6 
spellName: Snuff Life's Flame
spellCollege: [Fire]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "14"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Fire 3, Body Of Flames, ]
spellPrereqText: Magery 3, Fire 3, Body Of Flames
spellSource: Magic - Death Spells
spellReference: MDS12
spellLink: [[Magic - Death Spells.pdf#page=12&search=Snuff Life's Flame]]
spellPoints: 1
spellTags: Fire
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=12&search=Snuff Life's Flame|Spell Link]]

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