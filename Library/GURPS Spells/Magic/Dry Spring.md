---
tags:
  - Spell
  - SpellsAsMagic
spellID: pEq2ZBWd90LyayEMk 
spellName: Dry Spring
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 min"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Shape Earth, Destroy Water, ]
spellPrereqText: Shape Earth, Destroy Water
spellSource: Magic
spellReference: M188
spellLink: [[Magic.pdf#page=190&search=Dry Spring]]
spellPoints: 1
spellTags: Water
spellWeapons: 
---

 [[Magic.pdf#page=190&search=Dry Spring|Spell Link]]

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