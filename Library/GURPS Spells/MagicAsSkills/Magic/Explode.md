---
tags:
  - Spell
  - SpellsAsMagic
spellID: pUx0unqgm10djasM5 
spellName: Explode
spellCollege: [Making & Breaking]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instant"'
spellCastingTime: '"1 sec"'
spellCost: "2-6"
spellMaintenance: "-"
spellPrerequisites: [Shatter, Apportation, Magery 2, Making & Breaking 2, ]
spellPrereqText: Shatter, Apportation, Magery 2, Making & Breaking 2
spellSource: Magic
spellReference: M118
spellLink: [[Magic.pdf#page=120&search=Explode]]
spellPoints: 1
spellTags: Making & Breaking
spellWeapons: [{"id":"w9os3CLqAck-65EjK","damage":{"type":"frag/2 points","base":"1d"},"calc":{"damage":"1d frag/2 points"}}]
---

 [[Magic.pdf#page=120&search=Explode|Spell Link]]

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