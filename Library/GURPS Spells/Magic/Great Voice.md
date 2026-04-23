---
tags:
  - Spell
  - SpellsAsMagic
spellID: pzvtbf3U5A7yHxQSg 
spellName: Great Voice
spellCollege: [Sound]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"2 sec"'
spellCost: "3"
spellMaintenance: "1"
spellPrerequisites: [Thunderclap, Voices, ]
spellPrereqText: Thunderclap, Voices
spellSource: Magic
spellReference: M173
spellLink: [[Magic.pdf#page=175&search=Great Voice]]
spellPoints: 1
spellTags: Sound
spellWeapons: 
---

 [[Magic.pdf#page=175&search=Great Voice|Spell Link]]

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