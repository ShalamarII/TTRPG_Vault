---
tags:
  - Spell
  - SpellsAsMagic
spellID: pRlgDFWqH96ddfy6M 
spellName: Death Field
spellCollege: [Body Control]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: HT
spellDuration: '"Intantaneous"'
spellCastingTime: '"1/2 base cost"'
spellCost: "2/1d"
spellMaintenance: "undefined"
spellPrerequisites: [Deathtouch, Magery4, 10 Spell(s) from the Body Control College, ]
spellPrereqText: Deathtouch, Magery4, 10 Spell(s) from the Body Control College
spellSource: Magic - Artillery Spells
spellReference: MAS11
spellLink: [[Magic - Artillery Spells.pdf#page=11&search=Death Field]]
spellPoints: 1
spellTags: Artillery, Body Control
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=11&search=Death Field|Spell Link]]

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