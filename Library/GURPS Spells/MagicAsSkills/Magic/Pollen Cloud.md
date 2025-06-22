---
tags:
  - Spell
  - SpellsAsMagic
spellID: poaIKDCgfPyu9t52H 
spellName: Pollen Cloud
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: HT
spellDuration: '"5 min#"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [Shape Plant, ]
spellPrereqText: Shape Plant
spellSource: Magic
spellReference: M162
spellLink: [[Magic.pdf#page=164&search=Pollen Cloud]]
spellPoints: 1
spellTags: Plant
spellWeapons: [{"id":"wBFuWNp2jVMi8Cdmb","damage":{"type":"Cough/Sneeze"},"usage":"Area","calc":{"damage":"Cough/Sneeze"}}]
---

 [[Magic.pdf#page=164&search=Pollen Cloud|Spell Link]]

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