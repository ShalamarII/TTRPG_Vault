---
tags:
  - Spell
  - SpellsAsMagic
spellID: ptTRbSLNCarbaCkfS 
spellName: Improved Explosive Fireball
spellCollege: [Fire]
spellDifficulty: IQ/VH
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1-3 secs"'
spellCost: "3-3xMagery#"
spellMaintenance: "undefined"
spellPrerequisites: [10 Spell(s) from the Fire College, Magery4, Explosive Fireball, ]
spellPrereqText: 10 Spell(s) from the Fire College, Magery4, Explosive Fireball
spellSource: Magic - Artillery Spells
spellReference: MAS15
spellLink: [[Magic - Artillery Spells.pdf#page=15&search=Improved Explosive Fireball]]
spellPoints: 1
spellTags: Artillery, Fire
spellWeapons: [{"id":"WpCAzypuh8K7MpUP5","damage":{"type":"burn ex/3 points","base":"1d"},"accuracy":"2","range":"50/100","rate_of_fire":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Projectile"}],"calc":{"damage":"1d burn ex/3 points"}}]
---

 [[Magic - Artillery Spells.pdf#page=15&search=Improved Explosive Fireball|Spell Link]]

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