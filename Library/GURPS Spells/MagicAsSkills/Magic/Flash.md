---
tags:
  - Spell
  - SpellsAsMagic
spellID: pSCZpoR2IcjVu2EKl 
spellName: Flash
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Instant"'
spellCastingTime: '"2 sec"'
spellCost: "4"
spellMaintenance: "-"
spellPrerequisites: [Continual Light, ]
spellPrereqText: Continual Light
spellSource: Magic
spellReference: M112
spellLink: [[Magic.pdf#page=114&search=Flash]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: [{"id":"woKwNYTNHs9W8qegr","damage":{"type":"Blinds"},"usage":"Area","calc":{"damage":"Blinds"}}]
---

 [[Magic.pdf#page=114&search=Flash|Spell Link]]

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