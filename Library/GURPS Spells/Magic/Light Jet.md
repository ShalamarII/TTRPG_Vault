---
tags:
  - Spell
  - SpellsAsMagic
spellID: pS9F6yfG9fFaWddbJ 
spellName: Light Jet
spellCollege: [Light & Darkness]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "2"
spellMaintenance: "1"
spellPrerequisites: [Continual Light, Shape Light, ]
spellPrereqText: Continual Light, Shape Light
spellSource: Magic
spellReference: M112
spellLink: [[Magic.pdf#page=114&search=Light Jet]]
spellPoints: 1
spellTags: Light & Darkness
spellWeapons: [{"id":"wMO9Q7zgMO75W6BYw","damage":{"type":"Blinds"},"usage":"Jet","reach":"10","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"Blinds"}}]
---

 [[Magic.pdf#page=114&search=Light Jet|Spell Link]]

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