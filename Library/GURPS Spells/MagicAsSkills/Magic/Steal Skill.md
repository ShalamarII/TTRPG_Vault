---
tags:
  - Spell
  - SpellsAsMagic
spellID: pdJ77OYgqGk6ItcEc 
spellName: Steal Skill
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will
spellDuration: '"24 hrs"'
spellCastingTime: '"1 min"'
spellCost: "1 per CP stolen"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Necromancy 3, Borrow Skill, Daze, ]
spellPrereqText: Magery 3, Necromancy 3, Borrow Skill, Daze
spellSource: Magic
spellReference: M158
spellLink: [[Magic.pdf#page=160&search=Steal Skill]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=160&search=Steal Skill|Spell Link]]

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