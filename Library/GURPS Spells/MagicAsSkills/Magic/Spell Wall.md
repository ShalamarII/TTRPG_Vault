---
tags:
  - Spell
  - SpellsAsMagic
spellID: pd6YCdgbPjpAYOV2y 
spellName: Spell Wall
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Spells cast through it
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "2/1 yard wall"
spellMaintenance: "Same"
spellPrerequisites: [Spell Shield, ]
spellPrereqText: Spell Shield
spellSource: Magic
spellReference: M124
spellLink: [[Magic.pdf#page=126&search=Spell Wall]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=126&search=Spell Wall|Spell Link]]

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