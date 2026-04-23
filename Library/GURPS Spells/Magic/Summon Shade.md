---
tags:
  - Spell
  - SpellsAsMagic
spellID: pAbYBQ8ISQubYQZrC 
spellName: Summon Shade
spellCollege: [Knowledge]
spellDifficulty: IQ/VH
spellClass: Info
spellResisted: Will
spellDuration: '"1 min"'
spellCastingTime: '"10 min"'
spellCost: "50"
spellMaintenance: "20"
spellPrerequisites: [Summon Spirit, Divination, ]
spellPrereqText: Summon Spirit, Divination
spellSource: Magic
spellReference: M102
spellLink: [[Magic.pdf#page=104&search=Summon Shade]]
spellPoints: 1
spellTags: Knowledge
spellWeapons: 
---

 [[Magic.pdf#page=104&search=Summon Shade|Spell Link]]

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