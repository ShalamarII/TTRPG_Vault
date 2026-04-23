---
tags:
  - Spell
  - SpellsAsMagic
spellID: pKRjZrK3FGWy7ZS7B 
spellName: Acid Ball
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1-3 sec"'
spellCost: "1-Magery"
spellMaintenance: "-"
spellPrerequisites: [Create Acid, Magery 2, Water 2, ]
spellPrereqText: Create Acid, Magery 2, Water 2
spellSource: Magic
spellReference: M191
spellLink: [[Magic.pdf#page=193&search=Acid Ball]]
spellPoints: 1
spellTags: Water
spellWeapons: [{"id":"WpGKwl0MxSZnC6zvU","damage":{"type":"cor/point","base":"1d"},"accuracy":"1","range":"20/40","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"1d cor/point"}}]
---

 [[Magic.pdf#page=193&search=Acid Ball|Spell Link]]

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