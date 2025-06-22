---
tags:
  - Spell
  - SpellsAsMagic
spellID: pdDa0zCp6hpk1MI_E 
spellName: Flaming Armor
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "6"
spellMaintenance: "Half"
spellPrerequisites: [Magery 1, Fire 1, Flame Jet, Resist Fire, ]
spellPrereqText: Magery 1, Fire 1, Flame Jet, Resist Fire
spellSource: Magic
spellReference: M75
spellLink: [[Magic.pdf#page=77&search=Flaming Armor]]
spellPoints: 1
spellTags: Fire
spellWeapons: 
---

 [[Magic.pdf#page=77&search=Flaming Armor|Spell Link]]

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