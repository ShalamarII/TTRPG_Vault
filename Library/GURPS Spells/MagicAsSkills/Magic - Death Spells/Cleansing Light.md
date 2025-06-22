---
tags:
  - Spell
  - SpellsAsMagic
spellID: pd8jzd3J-SYZBan8o 
spellName: Cleansing Light
spellCollege: [Light & Darkness]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 minute or until a target is hit"'
spellCastingTime: '"3 sec"'
spellCost: "13-16"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Light & Darkness 3, Sunbolt, Light Jet, Flash, 10 Spell(s) from the Light & Darkness College, ]
spellPrereqText: Magery 3, Light & Darkness 3, Sunbolt, Light Jet, Flash, 10 Spell(s) from the Light & Darkness College
spellSource: Magic - Death Spells
spellReference: MDS16
spellLink: [[Magic - Death Spells.pdf#page=16&search=Cleansing Light]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: 
---

 [[Magic - Death Spells.pdf#page=16&search=Cleansing Light|Spell Link]]

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