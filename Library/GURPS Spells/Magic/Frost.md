---
tags:
  - Spell
  - SpellsAsMagic
spellID: p_t25cjDNPBpLo1Nv 
spellName: Frost
spellCollege: [Water, Weather]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"Indef"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [Cold, Create Water, ]
spellPrereqText: Cold, Create Water
spellSource: Magic
spellReference: M193
spellLink: [[Magic.pdf#page=195&search=Frost]]
spellPoints: 1
spellTags: Water, Weather
spellWeapons: 
---

 [[Magic.pdf#page=195&search=Frost|Spell Link]]

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