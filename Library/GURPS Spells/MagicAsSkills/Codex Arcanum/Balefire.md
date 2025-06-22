---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Balefire
spellCollege: [Fire]
spellDifficulty: 
spellClass: Regular
spellResisted: 
spellDuration: '"1 second; burning may continue."'
spellCastingTime: '""'
spellCost: "1 to 3 points. Does 1d-1 damage for each point put into it. The Balefire's range in hexes"
spellMaintenance: "1 to maintain"
spellPrerequisites: [Magery 2, Essential Flame, Shape Fire]
spellPrereqText: Magery 2, Essential Flame, Shape Fire
spellSource: Codex Arcanum
spellReference: GOCA198
spellLink: [[Codex Arcanum.pdf#page=198&search=Balefire]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=198&search=Balefire|Spell Link]]

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