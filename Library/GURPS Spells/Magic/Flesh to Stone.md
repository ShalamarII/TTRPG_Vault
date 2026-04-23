---
tags:
  - Spell
  - SpellsAsMagic
spellID: p9CvoJ8L5UejAof_Q 
spellName: Flesh to Stone
spellCollege: [Earth]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"2 sec"'
spellCost: "10#"
spellMaintenance: "-"
spellPrerequisites: [Earth To Stone, ]
spellPrereqText: Earth To Stone
spellSource: Magic
spellReference: M51
spellLink: [[Magic.pdf#page=53&search=Flesh to Stone]]
spellPoints: 1
spellTags: Earth
spellWeapons: 
---

 [[Magic.pdf#page=53&search=Flesh to Stone|Spell Link]]

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