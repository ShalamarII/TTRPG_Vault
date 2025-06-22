---
tags:
  - Spell
  - SpellsAsMagic
spellID: pja3RJ8dKtVHLXbtO 
spellName: Sun's Arc
spellCollege: [Light & Darkness]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1-3 secs"'
spellCost: "5/1d"
spellMaintenance: "undefined"
spellPrerequisites: [10 Spell(s) from the Light & Darkness College, Light Jet, Sunbolt, Magery4, ]
spellPrereqText: 10 Spell(s) from the Light & Darkness College, Light Jet, Sunbolt, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS18
spellLink: [[Magic - Artillery Spells.pdf#page=18&search=Sun's Arc]]
spellPoints: 1
spellTags: Artillery, Light & Darkness
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=18&search=Sun's Arc|Spell Link]]

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