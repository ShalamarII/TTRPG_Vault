---
tags:
  - Spell
  - SpellsAsMagic
spellID: pplfbsv9TNTQHWYhp 
spellName: Preserve Food
spellCollege: [Food]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 week"'
spellCastingTime: '"1 sec"'
spellCost: "2/lb"
spellMaintenance: "Half"
spellPrerequisites: [Decay, ]
spellPrereqText: Decay
spellSource: Magic
spellReference: M79
spellLink: [[Magic.pdf#page=81&search=Preserve Food]]
spellPoints: 1
spellTags: Food
spellWeapons: 
---

 [[Magic.pdf#page=81&search=Preserve Food|Spell Link]]

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