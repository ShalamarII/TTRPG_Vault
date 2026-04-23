---
tags:
  - Spell
  - SpellsAsMagic
spellID: pDGfNX9L4zZoqq8cI 
spellName: Fling Fruit
spellCollege: [Movement, Plant]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1 or 2"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Movement 1, Plant 1, Shape Plant, Apportation, ]
spellPrereqText: Magery 1, Movement 1, Plant 1, Shape Plant, Apportation
spellSource: Magic - Plant Spells
spellReference: MPS13
spellLink: [[Magic - Plant Spells.pdf#page=13&search=Fling Fruit]]
spellPoints: 1
spellTags: Movement, Plant
spellWeapons: [{"id":"WDe3qGQFOIsY9pXnj","damage":{"type":"Special cr"},"accuracy":"1","range":"20/60","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Throwing"}],"calc":{"damage":"Special cr"}}]
---

 [[Magic - Plant Spells.pdf#page=13&search=Fling Fruit|Spell Link]]

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