---
tags:
  - Spell
  - SpellsAsMagic
spellID: pHMbJXwGI15n537gN 
spellName: Protect Animal
spellCollege: [Animal]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 min"'
spellCost: "1"
spellMaintenance: "1"
spellPrerequisites: [3 Spell(s) from the Animal College, Watchdog, Armor, ]
spellPrereqText: 3 Spell(s) from the Animal College, Watchdog, Armor
spellSource: Magic
spellReference: M32
spellLink: [[Magic.pdf#page=34&search=Protect Animal]]
spellPoints: 1
spellTags: Animal
spellWeapons: 
---

 [[Magic.pdf#page=34&search=Protect Animal|Spell Link]]

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