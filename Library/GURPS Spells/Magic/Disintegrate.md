---
tags:
  - Spell
  - SpellsAsMagic
spellID: p-aNLiby3uTCSKeO4 
spellName: Disintegrate
spellCollege: [Making & Breaking]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec"'
spellCost: "1-4"
spellMaintenance: "-"
spellPrerequisites: [Shatter, Ruin, Earth To Air, Destroy Air, Destroy Water, Magery 2, Making & Breaking 2, ]
spellPrereqText: Shatter, Ruin, Earth To Air, Destroy Air, Destroy Water, Magery 2, Making & Breaking 2
spellSource: Magic
spellReference: M120
spellLink: [[Magic.pdf#page=122&search=Disintegrate]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: [{"id":"wz1xellybGpXelQIx","damage":{"type":"/point","base":"1d"},"calc":{"damage":"1d /point"}}]
---

 [[Magic.pdf#page=122&search=Disintegrate|Spell Link]]

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