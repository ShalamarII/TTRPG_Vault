---
tags:
  - Spell
  - SpellsAsMagic
spellID: p4q99Db3jJ0SoLFtu 
spellName: Null Sphere
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Missile
spellResisted: undefined
spellDuration: undefined
spellCastingTime: '"1-3 secs"'
spellCost: "4-4×Magery#"
spellMaintenance: "undefined"
spellPrerequisites: [Create Gate, Magery5, ]
spellPrereqText: Create Gate, Magery5
spellSource: Magic - Artillery Spells
spellReference: MAS16
spellLink: [[Magic - Artillery Spells.pdf#page=16&search=Null Sphere]]
spellPoints: 1
spellTags: Artillery, Gate
spellWeapons: [{"id":"WbGaHxMYjsbx2E4HF","damage":{"type":"Special"},"accuracy":"2","range":"40/80","rate_of_fire":"1","recoil":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"Special"}}]
---

 [[Magic - Artillery Spells.pdf#page=16&search=Null Sphere|Spell Link]]

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