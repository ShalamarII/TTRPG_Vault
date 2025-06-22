---
tags:
  - Spell
  - SpellsAsMagic
spellID: pQx00Q5mmSrztDp6f 
spellName: Wood Golem
spellCollege: [Enchantment, Plant]
spellDifficulty: IQ/VH
spellClass: Enchantment
spellResisted: undefined
spellDuration: '"Permanent"'
spellCastingTime: '"Varies"'
spellCost: "360"
spellMaintenance: "-"
spellPrerequisites: [Animation, Shape Plant, Enchant, ]
spellPrereqText: Animation, Shape Plant, Enchant
spellSource: Magic - Plant Spells
spellReference: MPS13
spellLink: [[Magic - Plant Spells.pdf#page=13&search=Wood Golem]]
spellPoints: 1
spellTags: Enchantment, Plant
spellWeapons: 
---

 [[Magic - Plant Spells.pdf#page=13&search=Wood Golem|Spell Link]]

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