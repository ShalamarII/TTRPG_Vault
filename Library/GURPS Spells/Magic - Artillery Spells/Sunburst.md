---
tags:
  - Spell
  - SpellsAsMagic
spellID: p2Lm-fNJYUSVM99Kq 
spellName: Sunburst
spellCollege: [Light & Darkness]
spellDifficulty: IQ/VH
spellClass: Missile
spellResisted: undefined
spellDuration: undefined
spellCastingTime: '"1-3 secs"'
spellCost: "2-2×Magery#"
spellMaintenance: "undefined"
spellPrerequisites: [10 Spell(s) from the Light & Darkness College, Flash, Sunbolt, Magery3, ]
spellPrereqText: 10 Spell(s) from the Light & Darkness College, Flash, Sunbolt, Magery3
spellSource: Magic - Artillery Spells
spellReference: MAS18
spellLink: [[Magic - Artillery Spells.pdf#page=18&search=Sunburst]]
spellPoints: 1
spellTags: Artillery, Light & Darkness
spellWeapons: [{"id":"W7SeptTzMNCbhY5dE","damage":{"type":"Special"},"accuracy":"1","range":"25/50","rate_of_fire":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"Special"}}]
---

 [[Magic - Artillery Spells.pdf#page=18&search=Sunburst|Spell Link]]

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