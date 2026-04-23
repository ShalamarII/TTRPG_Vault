---
tags:
  - Spell
  - SpellsAsMagic
spellID: p23dHSFVDNw-fy6bG 
spellName: Suspended Animation
spellCollege: [Healing]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Until Awakened"'
spellCastingTime: '"30 sec"'
spellCost: "6"
spellMaintenance: "-"
spellPrerequisites: [Sleep, 4 Spell(s) from the Healing College, ]
spellPrereqText: Sleep, 4 Spell(s) from the Healing College
spellSource: Magic
spellReference: M94
spellLink: [[Magic.pdf#page=96&search=Suspended Animation]]
spellPoints: 1
spellTags: Healing
spellWeapons: 
---

 [[Magic.pdf#page=96&search=Suspended Animation|Spell Link]]

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