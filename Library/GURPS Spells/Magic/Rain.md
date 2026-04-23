---
tags:
  - Spell
  - SpellsAsMagic
spellID: pQbSj8iMCPqfXSwFk 
spellName: Rain
spellCollege: [Air, Water, Weather]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"1 min"'
spellCost: "1/10#"
spellMaintenance: "Same"
spellPrerequisites: [Clouds, ]
spellPrereqText: Clouds
spellSource: Magic
spellReference: M195
spellLink: [[Magic.pdf#page=197&search=Rain]]
spellPoints: 1
spellTags: Air, Water, Weather
spellWeapons: 
---

 [[Magic.pdf#page=197&search=Rain|Spell Link]]

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