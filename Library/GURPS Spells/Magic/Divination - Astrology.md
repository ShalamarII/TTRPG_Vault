---
tags:
  - Spell
  - SpellsAsMagic
spellID: piMdAVGiagmafYIbg 
spellName: Divination - Astrology
spellCollege: [Knowledge]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 hr"'
spellCost: "10"
spellMaintenance: "-"
spellPrerequisites: [History, Predict Weather, at least 15 Astronomy, ]
spellPrereqText: History, Predict Weather, at least 15 Astronomy
spellSource: Magic
spellReference: M108
spellLink: [[Magic.pdf#page=110&search=Divination - Astrology]]
spellPoints: 1
spellTags: Knowledge
spellWeapons: 
---

 [[Magic.pdf#page=110&search=Divination - Astrology|Spell Link]]

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