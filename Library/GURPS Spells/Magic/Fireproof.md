---
tags:
  - Spell
  - SpellsAsMagic
spellID: pnNY8NwPt5iqDDgpS 
spellName: Fireproof
spellCollege: [Fire]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 day"'
spellCastingTime: '"5 min"'
spellCost: "3#"
spellMaintenance: "Same"
spellPrerequisites: [Extinguish Fire, ]
spellPrereqText: Extinguish Fire
spellSource: Magic
spellReference: M73
spellLink: [[Magic.pdf#page=75&search=Fireproof]]
spellPoints: 1
spellTags: Fire
spellWeapons: 
---

 [[Magic.pdf#page=75&search=Fireproof|Spell Link]]

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