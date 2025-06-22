---
tags:
  - Spell
  - SpellsAsMagic
spellID: pMw1sdh68BoUGdUUw 
spellName: Skull-Spirit
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"24 hrs"'
spellCastingTime: '"1 sec"'
spellCost: "20"
spellMaintenance: "-"
spellPrerequisites: [4 Spell(s) from the Necromancy College, ]
spellPrereqText: 4 Spell(s) from the Necromancy College
spellSource: Magic
spellReference: M151
spellLink: [[Magic.pdf#page=153&search=Skull-Spirit]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=153&search=Skull-Spirit|Spell Link]]

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