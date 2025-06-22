---
tags:
  - Spell
  - SpellsAsMagic
spellID: pXstRtVSI4jJ6QgDw 
spellName: Strike Barren
spellCollege: [Body Control, Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: HT
spellDuration: '"Permanent"'
spellCastingTime: '"30 sec"'
spellCost: "5"
spellMaintenance: "-"
spellPrerequisites: [Magery 1, Body Control 1, Necromancy 1, Steal Vitality, Decay, ]
spellPrereqText: Magery 1, Body Control 1, Necromancy 1, Steal Vitality, Decay
spellSource: Magic
spellReference: M41
spellLink: [[Magic.pdf#page=43&search=Strike Barren]]
spellPoints: 1
spellTags: Body Control, Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=43&search=Strike Barren|Spell Link]]

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