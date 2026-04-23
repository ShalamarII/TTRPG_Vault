---
tags:
  - Spell
  - SpellsAsMagic
spellID: pktuIKFp25cgbVnu6 
spellName: Plane Shift Other (@plane@)
spellCollege: [Gate]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: Will+1
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "20"
spellMaintenance: "-"
spellPrerequisites: [Magery 3, Gate 3, Plane Shift (@plane@), ]
spellPrereqText: Magery 3, Gate 3, Plane Shift (@plane@)
spellSource: Magic
spellReference: M83
spellLink: [[Magic.pdf#page=85&search=Plane Shift Other (@plane@)]]
spellPoints: 1
spellTags: Gate
spellWeapons: 
---

 [[Magic.pdf#page=85&search=Plane Shift Other (@plane@)|Spell Link]]

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