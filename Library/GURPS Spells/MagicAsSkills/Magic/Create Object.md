---
tags:
  - Spell
  - SpellsAsMagic
spellID: p9_7eHEt41sPnSc7F 
spellName: Create Object
spellCollege: [Illusion & Creation]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"While touching someone"'
spellCastingTime: '"1 sec/cost"'
spellCost: "2/5 lbs"
spellMaintenance: "-"
spellPrerequisites: [Create Earth, Perfect Illusion, Magery 2, Illusion & Creation 2, ]
spellPrereqText: Create Earth, Perfect Illusion, Magery 2, Illusion & Creation 2
spellSource: Magic
spellReference: M98
spellLink: [[Magic.pdf#page=100&search=Create Object]]
spellPoints: 1
spellTags: Illusion & Creation
spellWeapons: 
---

 [[Magic.pdf#page=100&search=Create Object|Spell Link]]

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