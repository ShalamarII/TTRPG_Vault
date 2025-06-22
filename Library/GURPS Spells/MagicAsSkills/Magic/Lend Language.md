---
tags:
  - Spell
  - SpellsAsMagic
spellID: pd08yPQC8wj58T03p 
spellName: Lend Language
spellCollege: [Communication & Empathy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"3 sec"'
spellCost: "3"
spellMaintenance: "1"
spellPrerequisites: [3 Spell(s) from the Communication & Empathy College, Beast Speech, ]
spellPrereqText: 3 Spell(s) from the Communication & Empathy College, Beast Speech
spellSource: Magic
spellReference: M46
spellLink: [[Magic.pdf#page=48&search=Lend Language]]
spellPoints: 1
spellTags: Communication & Empathy
spellWeapons: 
---

 [[Magic.pdf#page=48&search=Lend Language|Spell Link]]

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