---
tags:
  - Spell
  - SpellsAsMagic
spellID: p6zHwu5gJcy7psObZ 
spellName: Frostbite
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Permanent"'
spellCastingTime: '"3 sec"'
spellCost: "1-3"
spellMaintenance: "-"
spellPrerequisites: [Freeze, Frost, ]
spellPrereqText: Freeze, Frost
spellSource: Magic
spellReference: M189
spellLink: [[Magic.pdf#page=191&search=Frostbite]]
spellPoints: 1
spellTags: Water
spellWeapons: [{"id":"wxA_WaCFw_rdyrrXu","damage":{"type":"freezing/point","base":"1d"},"calc":{"damage":"1d freezing/point"}}]
---

 [[Magic.pdf#page=191&search=Frostbite|Spell Link]]

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