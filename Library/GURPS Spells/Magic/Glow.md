---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVN4sxGbV5XENcxGe 
spellName: Glow
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"2d days"'
spellCastingTime: '"Varies"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Continual Light, ]
spellPrereqText: Continual Light
spellSource: Magic
spellReference: M112
spellLink: [[Magic.pdf#page=114&search=Glow]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Magic.pdf#page=114&search=Glow|Spell Link]]

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