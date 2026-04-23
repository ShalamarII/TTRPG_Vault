---
tags:
  - Spell
  - SpellsAsMagic
spellID: pvJEJj-ff63Pdr_VE 
spellName: Bless Plants
spellCollege: [Plant]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"1 Crop or Season"'
spellCastingTime: '"5 min"'
spellCost: "1 minimum"
spellMaintenance: "-"
spellPrerequisites: [Heal Plant, ]
spellPrereqText: Heal Plant
spellSource: Magic
spellReference: M161
spellLink: [[Magic.pdf#page=163&search=Bless Plants]]
spellPoints: 1
spellTags: Plant
spellWeapons: 
---

 [[Magic.pdf#page=163&search=Bless Plants|Spell Link]]

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