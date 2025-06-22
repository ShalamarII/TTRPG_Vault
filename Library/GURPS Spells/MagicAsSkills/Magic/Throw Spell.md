---
tags:
  - Spell
  - SpellsAsMagic
spellID: pXR2qnLY4Wv8q38Bq 
spellName: Throw Spell
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Missile/Special
spellResisted: undefined
spellDuration: '"Until thrown"'
spellCastingTime: '"1 sec"'
spellCost: "3"
spellMaintenance: "-"
spellPrerequisites: [Delay, Catch Spell, ]
spellPrereqText: Delay, Catch Spell
spellSource: Magic
spellReference: M128
spellLink: [[Magic.pdf#page=130&search=Throw Spell]]
spellPoints: 1
spellTags: Meta
spellWeapons: [{"id":"WEOtFlz1Xy44hS8pF","damage":{"type":"Special"},"accuracy":"1","range":"80","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"Special"}}]
---

 [[Magic.pdf#page=130&search=Throw Spell|Spell Link]]

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