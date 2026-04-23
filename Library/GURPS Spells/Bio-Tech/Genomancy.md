---
tags:
  - Spell
  - SpellsAsMagic
spellID: px1ehCWIdhOJTugcC 
spellName: Genomancy
spellCollege: [Knowledge]
spellDifficulty: IQ/H
spellClass: Information
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "undefined"
spellPrerequisites: [Analyze Heredity, 1 Spell(s) from the Healing College, 1 Spell(s) from the Body Control College, ]
spellPrereqText: Analyze Heredity, 1 Spell(s) from the Healing College, 1 Spell(s) from the Body Control College
spellSource: Bio-Tech
spellReference: BT31
spellLink: [[Bio-Tech.pdf#page=31&search=Genomancy]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Bio-Tech.pdf#page=31&search=Genomancy|Spell Link]]

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