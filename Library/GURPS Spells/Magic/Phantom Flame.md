---
tags:
  - Spell
  - SpellsAsMagic
spellID: pK6aJzd4Me5I3feJh 
spellName: Phantom Flame
spellCollege: [Fire, Illusion & Creation]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "1"
spellPrerequisites: [Shape Fire, Simple Illusion, ]
spellPrereqText: Shape Fire, Simple Illusion
spellSource: Magic
spellReference: M73
spellLink: [[Magic.pdf#page=75&search=Phantom Flame]]
spellPoints: 1
spellTags: Fire, Illusion & Creation
spellWeapons: 
---

 [[Magic.pdf#page=75&search=Phantom Flame|Spell Link]]

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