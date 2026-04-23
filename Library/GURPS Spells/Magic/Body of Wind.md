---
tags:
  - Spell
  - SpellsAsMagic
spellID: piW4_Db7F5KqdLk6- 
spellName: Body of Wind
spellCollege: [Air]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "8"
spellMaintenance: "4"
spellPrerequisites: [1 Spell(s) from 5 Colleges, Windstorm, Body Of Air, Magery 3, Air 3, ]
spellPrereqText: 1 Spell(s) from 5 Colleges, Windstorm, Body Of Air, Magery 3, Air 3
spellSource: Magic
spellReference: M27
spellLink: [[Magic.pdf#page=29&search=Body of Wind]]
spellPoints: 1
spellTags: Air
spellWeapons: 
---

 [[Magic.pdf#page=29&search=Body of Wind|Spell Link]]

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