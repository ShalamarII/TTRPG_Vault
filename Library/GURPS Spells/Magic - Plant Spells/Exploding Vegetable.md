---
tags:
  - Spell
  - SpellsAsMagic
spellID: p5rk0nW_tZm16gCnv 
spellName: Exploding Vegetable
spellCollege: [Making & Breaking, Plant]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "2-6"
spellMaintenance: "-"
spellPrerequisites: [Shape Plant, ]
spellPrereqText: Shape Plant
spellSource: Magic - Plant Spells
spellReference: MPS13
spellLink: [[Magic - Plant Spells.pdf#page=13&search=Exploding Vegetable]]
spellPoints: 1
spellTags: Making & Breaking, Plant
spellWeapons: [{"id":"w5HOvXfHVvNqMfiVC","damage":{"type":"frag/2 points","base":"1d"},"calc":{"damage":"1d frag/2 points"}}]
---

 [[Magic - Plant Spells.pdf#page=13&search=Exploding Vegetable|Spell Link]]

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