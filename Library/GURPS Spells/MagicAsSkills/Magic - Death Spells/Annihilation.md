---
tags:
  - Spell
  - SpellsAsMagic
spellID: pM3pvFGbXMT38wLAB 
spellName: Annihilation
spellCollege: [Making & Breaking]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"3 sec"'
spellCost: "8-14"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Making & Breaking 3, Deathtouch, Steal Vitality, Disintegrate, ]
spellPrereqText: Magery 3, Making & Breaking 3, Deathtouch, Steal Vitality, Disintegrate
spellSource: Magic - Death Spells
spellReference: MDS16
spellLink: [[Magic - Death Spells.pdf#page=16&search=Annihilation]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=16&search=Annihilation|Spell Link]]

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