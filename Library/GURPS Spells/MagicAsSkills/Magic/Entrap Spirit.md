---
tags:
  - Spell
  - SpellsAsMagic
spellID: pckWlaSeqift7z1-Z 
spellName: Entrap Spirit
spellCollege: [Necromancy]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"5 min"'
spellCastingTime: '"1 sec"'
spellCost: "Varies"
spellMaintenance: "Varies"
spellPrerequisites: [Soul Jar, Turn Spirit, Magery 1, Necromancy 1, ]
spellPrereqText: Soul Jar, Turn Spirit, Magery 1, Necromancy 1
spellSource: Magic
spellReference: M157
spellLink: [[Magic.pdf#page=159&search=Entrap Spirit]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=159&search=Entrap Spirit|Spell Link]]

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