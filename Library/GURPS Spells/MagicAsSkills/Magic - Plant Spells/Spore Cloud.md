---
tags:
  - Spell
  - SpellsAsMagic
spellID: pg44ChoyV8dpxS0Ab 
spellName: Spore Cloud
spellCollege: [Fungus]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"5 min#"'
spellCastingTime: '"1 sec"'
spellCost: "1"
spellMaintenance: "-"
spellPrerequisites: [Fungus Growth, ]
spellPrereqText: Fungus Growth
spellSource: Magic - Plant Spells
spellReference: MPS17
spellLink: [[Magic - Plant Spells.pdf#page=17&search=Spore Cloud]]
spellPoints: 1
spellTags: Fungus
spellWeapons: [{"id":"w8f72ZeUzpiIz1qwA","damage":{"type":"Cough/Sneeze"},"usage":"Area","calc":{"damage":"Cough/Sneeze"}}]
---

 [[Magic - Plant Spells.pdf#page=17&search=Spore Cloud|Spell Link]]

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