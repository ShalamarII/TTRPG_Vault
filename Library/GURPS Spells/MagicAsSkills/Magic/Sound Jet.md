---
tags:
  - Spell
  - SpellsAsMagic
spellID: p0cqGtgBnRDdFhrd1 
spellName: Sound Jet
spellCollege: [Sound]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec"'
spellCost: "1-4"
spellMaintenance: "1-4"
spellPrerequisites: [Great Voice, ]
spellPrereqText: Great Voice
spellSource: Magic
spellReference: M173
spellLink: [[Magic.pdf#page=175&search=Sound Jet]]
spellPoints: 1
spellTags: Sound
spellWeapons: [{"id":"wdX7LCtUpXqn1XcQ9","damage":{"type":"Stuns"},"usage":"Jet","reach":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"Stuns"}}]
---

 [[Magic.pdf#page=175&search=Sound Jet|Spell Link]]

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