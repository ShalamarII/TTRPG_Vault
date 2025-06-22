---
tags:
  - Spell
  - SpellsAsMagic
spellID: pM8o1DVdpOHJs6tEz 
spellName: Mass Resist Acid
spellCollege: [Protection & Warning, Water]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 minute"'
spellCastingTime: '"1 sec/energy point"'
spellCost: "2; 6 to resist Essential Acid"
spellMaintenance: "Half"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Pyramid 3 - 4
spellReference: PY4:9
spellLink: [[Pyramid 3 - 4.pdf#page=9&search=Mass Resist Acid]]
spellPoints: 1
spellTags: Protection & Warning, Secret, Water
spellWeapons: 
---

 [[Pyramid 3 - 4.pdf#page=9&search=Mass Resist Acid|Spell Link]]

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