---
tags:
  - Spell
  - SpellsAsMagic
spellID: p16g7ZAS19n67TLyq 
spellName: Duplicate
spellCollege: [Illusion & Creation]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"While touching someone"'
spellCastingTime: '"1 sec/cost"'
spellCost: "3/5 lbs"
spellMaintenance: "-"
spellPrerequisites: [Copy, Create Earth, ]
spellPrereqText: Copy, Create Earth
spellSource: Magic
spellReference: M98
spellLink: [[Magic.pdf#page=100&search=Duplicate]]
spellPoints: 1
spellTags: Illusion & Creation
spellWeapons: 
---

 [[Magic.pdf#page=100&search=Duplicate|Spell Link]]

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