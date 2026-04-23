---
tags:
  - Spell
  - SpellsAsMagic
spellID: pKeQZkFmRcEW8W2Zd 
spellName: Devitalize Air
spellCollege: [Air]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"Varies"'
spellCastingTime: '"1 sec"'
spellCost: "2"
spellMaintenance: "-"
spellPrerequisites: [Destroy Air, ]
spellPrereqText: Destroy Air
spellSource: Magic
spellReference: M25
spellLink: [[Magic.pdf#page=27&search=Devitalize Air]]
spellPoints: 1
spellTags: Air
spellWeapons: 
---

 [[Magic.pdf#page=27&search=Devitalize Air|Spell Link]]

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