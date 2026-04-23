---
tags:
  - Spell
  - SpellsAsMagic
spellID: pksRBeYiHUjK7O5V5 
spellName: Water Vision
spellCollege: [Knowledge, Water]
spellDifficulty: IQ/H
spellClass: Info
spellResisted: undefined
spellDuration: '"30 sec"'
spellCastingTime: '"1 sec"'
spellCost: "1#"
spellMaintenance: "1"
spellPrerequisites: [Shape Water, ]
spellPrereqText: Shape Water
spellSource: Magic
spellReference: M187
spellLink: [[Magic.pdf#page=189&search=Water Vision]]
spellPoints: 1
spellTags: Knowledge, Water
spellWeapons: 
---

 [[Magic.pdf#page=189&search=Water Vision|Spell Link]]

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