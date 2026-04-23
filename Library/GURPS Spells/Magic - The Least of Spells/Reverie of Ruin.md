---
tags:
  - Spell
  - SpellsAsMagic
spellID: p5yHXz0qvnuYe3XSe 
spellName: Reverie of Ruin
spellCollege: [Necromantic]
spellDifficulty: IQ/A
spellClass: Information
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"(20-skill) sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS15
spellLink: [[Magic - The Least of Spells.pdf#page=15&search=Reverie of Ruin]]
spellPoints: 1
spellTags: Necromantic
spellWeapons: 
---

 [[Magic - The Least of Spells.pdf#page=15&search=Reverie of Ruin|Spell Link]]

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