---
tags:
  - Spell
  - SpellsAsMagic
spellID: p-L2XVisNFl3TnTVv 
spellName: Pentagram
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: Attempts to cross it
spellDuration: '"Permanent"'
spellCastingTime: '"1 sec/sq foot"'
spellCost: "1/sq foot"
spellMaintenance: "-"
spellPrerequisites: [Spell Shield, ]
spellPrereqText: Spell Shield
spellSource: Magic
spellReference: M124
spellLink: [[Magic.pdf#page=126&search=Pentagram]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Magic.pdf#page=126&search=Pentagram|Spell Link]]

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