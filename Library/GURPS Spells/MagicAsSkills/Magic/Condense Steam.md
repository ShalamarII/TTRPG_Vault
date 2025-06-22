---
tags:
  - Spell
  - SpellsAsMagic
spellID: pvi9cR_bdXshvXITe 
spellName: Condense Steam
spellCollege: [Water]
spellDifficulty: IQ/H
spellClass: Area
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"10 sec"'
spellCost: "2#"
spellMaintenance: "-"
spellPrerequisites: [Boil Water, Cold, ]
spellPrereqText: Boil Water, Cold
spellSource: Magic
spellReference: M189
spellLink: [[Magic.pdf#page=191&search=Condense Steam]]
spellPoints: 1
spellTags: Water
spellWeapons: 
---

 [[Magic.pdf#page=191&search=Condense Steam|Spell Link]]

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