---
tags:
  - Spell
  - SpellsAsMagic
spellID: pdq4aSEl-kLHKUW8G 
spellName: Mud Jet
spellCollege: [Earth, Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec"'
spellCost: "1-3"
spellMaintenance: "1-3"
spellPrerequisites: [Sand Jet, Create Water, Water Jet, Create Earth, ]
spellPrereqText: Sand Jet, Create Water, Water Jet, Create Earth
spellSource: Magic
spellReference: M52
spellLink: [[Magic.pdf#page=54&search=Mud Jet]]
spellPoints: 1
spellTags: Earth, Water
spellWeapons: [{"id":"wj2VCbsPNpOIiL0w1","damage":{"type":"kb/point - Blinds","base":"1d"},"usage":"Jet","reach":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d kb/point - Blinds"}}]
---

 [[Magic.pdf#page=54&search=Mud Jet|Spell Link]]

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