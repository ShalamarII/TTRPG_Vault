---
tags:
  - Spell
  - SpellsAsMagic
spellID: pwMwY2OK8J9J8eIjn 
spellName: Dehydrate
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Permanent"'
spellCastingTime: '"2 sec"'
spellCost: "1-3"
spellMaintenance: "-"
spellPrerequisites: [Destroy Water, 5 Spell(s) from the Water College, ]
spellPrereqText: Destroy Water, 5 Spell(s) from the Water College
spellSource: Magic
spellReference: M188
spellLink: [[Magic.pdf#page=190&search=Dehydrate]]
spellPoints: 1
spellTags: Water
spellWeapons: [{"id":"wKtJ3bFFIXwRp-zOe","damage":{"type":"dehydrate/point","base":"1d-1"},"calc":{"damage":"1d-1 dehydrate/point"}}]
---

 [[Magic.pdf#page=190&search=Dehydrate|Spell Link]]

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