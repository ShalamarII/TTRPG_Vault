---
tags:
  - Spell
  - SpellsAsMagic
spellID: pZH-ZGEuLWf_ijz6a 
spellName: Earth to Water
spellCollege: [Earth, Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec"'
spellCost: "1/25 cu ft#"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Earth 1, Water 1, Shape Earth, Create Water, ]
spellPrereqText: Magery 1, Earth 1, Water 1, Shape Earth, Create Water
spellSource: Magic
spellReference: M52
spellLink: [[Magic.pdf#page=54&search=Earth to Water]]
spellPoints: 1
spellTags: Earth, Water
spellWeapons: 
---

 [[Magic.pdf#page=54&search=Earth to Water|Spell Link]]

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