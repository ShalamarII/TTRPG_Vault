---
tags:
  - Spell
  - SpellsAsMagic
spellID: pBGc8lk3YosCl6v-4 
spellName: Vine to Snake
spellCollege: [Illusion & Creation, Plant]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec/cost"'
spellCost: "Varies"
spellMaintenance: "Half"
spellPrerequisites: [Magery 2, Illusion & Creation 2, Create Plant, ]
spellPrereqText: Magery 2, Illusion & Creation 2, Create Plant
spellSource: Magic - Plant Spells
spellReference: MPS13
spellLink: [[Magic - Plant Spells.pdf#page=13&search=Vine to Snake]]
spellPoints: 1
spellTags: Illusion & Creation, Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=13&search=Vine to Snake|Spell Link]]

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