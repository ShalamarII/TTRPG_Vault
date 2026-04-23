---
tags:
  - Spell
  - SpellsAsMagic
spellID: pPnlm9Ij0LaQTmIOy 
spellName: Acid Jet
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 sec"'
spellCastingTime: '"1 sec"'
spellCost: "1-3"
spellMaintenance: "1-3"
spellPrerequisites: [Magery 2, Water 2, Create Acid, Water Jet, ]
spellPrereqText: Magery 2, Water 2, Create Acid, Water Jet
spellSource: Magic
spellReference: M192
spellLink: [[Magic.pdf#page=194&search=Acid Jet]]
spellPoints: 1
spellTags: Water
spellWeapons: [{"id":"wtMphmJKhYR8m9ykS","damage":{"type":"cor/point","base":"1d-1"},"usage":"Jet","reach":"1","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"1d-1 cor/point"}}]
---

 [[Magic.pdf#page=194&search=Acid Jet|Spell Link]]

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