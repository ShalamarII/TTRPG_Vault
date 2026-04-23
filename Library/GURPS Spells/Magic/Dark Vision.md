---
tags:
  - Spell
  - SpellsAsMagic
spellID: pMCiOp98AW7-VSqYX 
spellName: Dark Vision
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "5"
spellMaintenance: "2"
spellPrerequisites: [Night Vision, Infravision, ]
spellPrereqText: Night Vision, Infravision
spellSource: Magic
spellReference: M111
spellLink: [[Magic.pdf#page=113&search=Dark Vision]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Magic.pdf#page=113&search=Dark Vision|Spell Link]]

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