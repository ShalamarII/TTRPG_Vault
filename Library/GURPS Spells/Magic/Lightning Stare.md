---
tags:
  - Spell
  - SpellsAsMagic
spellID: pp0MfZwF1GWGVY4bW 
spellName: Lightning Stare
spellCollege: [Air, Weather]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"2 sec"'
spellCost: "1-4"
spellMaintenance: "-"
spellPrerequisites: [Resist Lightning, Lightning, ]
spellPrereqText: Resist Lightning, Lightning
spellSource: Magic
spellReference: M198
spellLink: [[Magic.pdf#page=200&search=Lightning Stare]]
spellPoints: 1
spellTags: Air, Weather
spellWeapons: [{"id":"wCN0quVTcdn6lp9aR","damage":{"type":"burn/point","base":"1d"},"usage":"Gaze","reach":"2","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Gaze"}],"calc":{"damage":"1d burn/point"}}]
---

 [[Magic.pdf#page=200&search=Lightning Stare|Spell Link]]

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