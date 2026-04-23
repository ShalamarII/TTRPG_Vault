---
tags:
  - Spell
  - SpellsAsMagic
spellID: pkiRSPVf9-PXw2J4e 
spellName: Plague Touch
spellCollege: [Body Control, Necromancy]
spellDifficulty: IQ/VH
spellClass: Melee
spellResisted: undefined
spellDuration: '"Special"'
spellCastingTime: '"2 secs"'
spellCost: "Any multiple of 3"
spellMaintenance: "undefined"
spellPrerequisites: [Magery4, Deathtouch, Pestilence, Sense Foes, ]
spellPrereqText: Magery4, Deathtouch, Pestilence, Sense Foes
spellSource: Magic - Artillery Spells
spellReference: MAS11
spellLink: [[Magic - Artillery Spells.pdf#page=11&search=Plague Touch]]
spellPoints: 1
spellTags: Artillery, Body Control, Necromancy
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=11&search=Plague Touch|Spell Link]]

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