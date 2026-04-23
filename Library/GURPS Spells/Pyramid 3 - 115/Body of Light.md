---
tags:
  - Spell
  - SpellsAsMagic
spellID: pwOcY9IM0SCJovDWp 
spellName: Body of Light
spellCollege: [Light & Darkness]
spellDifficulty: IQ/VH
spellClass: Regular/R-HT
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "12"
spellMaintenance: "4"
spellPrerequisites: [Body Of Shadow, ]
spellPrereqText: Body Of Shadow
spellSource: Pyramid 3 - 115
spellReference: PY115:21
spellLink: [[Pyramid 3 - 115.pdf#page=21&search=Body of Light]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Pyramid 3 - 115.pdf#page=21&search=Body of Light|Spell Link]]

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