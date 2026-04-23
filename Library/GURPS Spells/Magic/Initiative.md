---
tags:
  - Spell
  - SpellsAsMagic
spellID: pGsPbaSilXhAJqwcE 
spellName: Initiative
spellCollege: [Illusion & Creation]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"10 sec"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Independence, Wisdom, ]
spellPrereqText: Independence, Wisdom
spellSource: Magic
spellReference: M97
spellLink: [[Magic.pdf#page=99&search=Initiative]]
spellPoints: 1
spellTags: Illusion & Creation
spellWeapons: 
---

 [[Magic.pdf#page=99&search=Initiative|Spell Link]]

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