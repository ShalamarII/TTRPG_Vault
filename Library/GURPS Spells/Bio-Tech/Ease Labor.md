---
tags:
  - Spell
  - SpellsAsMagic
spellID: pd46SK6tH8u6wXurX 
spellName: Ease Labor
spellCollege: [Body Control]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 hour"'
spellCastingTime: '"6 sec"'
spellCost: "4"
spellMaintenance: "2"
spellPrerequisites: [Lend Vitality, ]
spellPrereqText: Lend Vitality
spellSource: Bio-Tech
spellReference: BT31
spellLink: [[Bio-Tech.pdf#page=31&search=Ease Labor]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Bio-Tech.pdf#page=31&search=Ease Labor|Spell Link]]

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