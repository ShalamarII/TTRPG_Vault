---
tags:
  - Spell
  - SpellsAsMagic
spellID: phqN4Qndj5bzE-0s_ 
spellName: Ember
spellCollege: [Fire]
spellDifficulty: IQ/A
spellClass: Missile
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Magic - The Least of Spells
spellReference: MTLOS9
spellLink: [[Magic - The Least of Spells.pdf#page=9&search=Ember]]
spellPoints: 1
spellTags: Fire
spellWeapons: [{"id":"WJNVf6gT8VxpiON0z","damage":{"type":""},"accuracy":"1","range":"10","defaults":[{"type":"skill","name":"Innate Attack","specialization":"Projectile"},{"type":"dx","modifier":-4}]}]
---

 [[Magic - The Least of Spells.pdf#page=9&search=Ember|Spell Link]]

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