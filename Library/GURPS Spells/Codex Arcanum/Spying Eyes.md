---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Spying Eyes
spellCollege: [Knowledge]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 minute, plus 1 minute to 'read' each eye once the spell ends."'
spellCastingTime: '""'
spellCost: "5"
spellMaintenance: "2 to maintain"
spellPrerequisites: [Wizard Eye]
spellPrereqText: Wizard Eye
spellSource: Codex Arcanum
spellReference: GOCA299
spellLink: [[Codex Arcanum.pdf#page=299&search=Spying Eyes]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=299&search=Spying Eyes|Spell Link]]

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