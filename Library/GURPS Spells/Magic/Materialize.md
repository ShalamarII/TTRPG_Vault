---
tags:
  - Spell
  - SpellsAsMagic
spellID: pem-calBazKZKl28g 
spellName: Materialize
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: ST or IQ
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "5"
spellMaintenance: "5"
spellPrerequisites: [Summon Spirit, ]
spellPrereqText: Summon Spirit
spellSource: Magic
spellReference: M150
spellLink: [[Magic.pdf#page=152&search=Materialize]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=152&search=Materialize|Spell Link]]

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