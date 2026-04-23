---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVqSFcMUO0IJQxP8q 
spellName: Age
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: HT
spellDuration: '"Permanent"'
spellCastingTime: '"1 min"'
spellCost: "10 per year of aging"
spellMaintenance: "-"
spellPrerequisites: [Youth, 6 Spell(s) from the Necromancy College, ]
spellPrereqText: Youth, 6 Spell(s) from the Necromancy College
spellSource: Magic
spellReference: M154
spellLink: [[Magic.pdf#page=156&search=Age]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=156&search=Age|Spell Link]]

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