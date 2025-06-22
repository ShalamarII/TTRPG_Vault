---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVk9Mud2QNhnSS7tx 
spellName: Awaken Craft Spirit
spellCollege: [Making & Breaking, Necromancy]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"5 sec"'
spellCost: "3"
spellMaintenance: "1"
spellPrerequisites: [Inspired Creation, Sense Spirit, ]
spellPrereqText: Inspired Creation, Sense Spirit
spellSource: Magic
spellReference: M115
spellLink: [[Magic.pdf#page=117&search=Awaken Craft Spirit]]
spellPoints: 1
spellTags: Making & Breaking, Necromancy
spellWeapons: 
---

 [[Magic.pdf#page=117&search=Awaken Craft Spirit|Spell Link]]

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