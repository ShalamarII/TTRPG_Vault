---
tags:
  - Spell
  - SpellsAsMagic
spellID: px9i09mZwRYfSKk7y 
spellName: Zombie Summoning
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"4 sec"'
spellCost: "5"
spellMaintenance: "2"
spellPrerequisites: [Zombie, ]
spellPrereqText: Zombie
spellSource: Magic
spellReference: M152
spellLink: [[Magic.pdf#page=154&search=Zombie Summoning]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=154&search=Zombie Summoning|Spell Link]]

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