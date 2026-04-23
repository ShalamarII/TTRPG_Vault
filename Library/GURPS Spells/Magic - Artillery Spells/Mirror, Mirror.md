---
tags:
  - Spell
  - SpellsAsMagic
spellID: pGeQlzqtBXLFOvuLG 
spellName: Mirror, Mirror
spellCollege: [Illusion & Creation]
spellDifficulty: IQ/VH
spellClass: Area
spellResisted: Special
spellDuration: '"1 minute or phantoms destroyed"'
spellCastingTime: '"1 sec/yard"'
spellCost: "10"
spellMaintenance: "Half"
spellPrerequisites: [Initiative, Phantom, Magery4, ]
spellPrereqText: Initiative, Phantom, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS17
spellLink: [[Magic - Artillery Spells.pdf#page=17&search=Mirror, Mirror]]
spellPoints: 1
spellTags: Artillery, Illusion & Creation
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=17&search=Mirror, Mirror|Spell Link]]

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