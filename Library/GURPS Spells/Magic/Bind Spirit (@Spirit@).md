---
tags:
  - Spell
  - SpellsAsMagic
spellID: p6Tf3ZOb7Gyzbaetu 
spellName: Bind Spirit (@Spirit@)
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Spirit's IQ
spellDuration: '"Permanent"'
spellCastingTime: '"5 min"'
spellCost: "Varies"
spellMaintenance: "-"
spellPrerequisites: [Command Spirit (@spirit@), Soul Jar, ]
spellPrereqText: Command Spirit (@spirit@), Soul Jar
spellSource: Magic
spellReference: M158
spellLink: [[Magic.pdf#page=160&search=Bind Spirit (@Spirit@)]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=160&search=Bind Spirit (@Spirit@)|Spell Link]]

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