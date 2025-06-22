---
tags:
  - Spell
  - SpellsAsMagic
spellID: p8T3XLlqCw7QVMt2- 
spellName: Microwave Jet
spellCollege: [Technological]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec"'
spellCost: "1-3"
spellMaintenance: "1-3"
spellPrerequisites: [Radio Hearing, Light Jet, Heat, ]
spellPrereqText: Radio Hearing, Light Jet, Heat
spellSource: Pyramid 3 - 115
spellReference: PY115:22
spellLink: [[Pyramid 3 - 115.pdf#page=22&search=Microwave Jet]]
spellPoints: 1
spellTags: Energy
spellWeapons: [{"id":"wKKBkGBctlvse9gdg","damage":{"type":"burn/point","base":"1"},"usage":"Jet","reach":"1-3","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1 burn/point"}}]
---

 [[Pyramid 3 - 115.pdf#page=22&search=Microwave Jet|Spell Link]]

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