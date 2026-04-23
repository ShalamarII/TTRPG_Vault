---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBKJeOioZ2PqkM68c 
spellName: Repel Animal (Mammal)
spellCollege: [Animal]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 hr"'
spellCastingTime: '"10 sec"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Animal Control (@animal@), ]
spellPrereqText: Animal Control (@animal@)
spellSource: Magic
spellReference: M31
spellLink: [[Magic.pdf#page=33&search=Repel Animal (Mammal)]]
spellPoints: 1
spellTags: Animal
spellWeapons: 
---

 [[Magic.pdf#page=33&search=Repel Animal (Mammal)|Spell Link]]

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