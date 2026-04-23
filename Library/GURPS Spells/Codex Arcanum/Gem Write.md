---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Gem Write
spellCollege: [Enchantment]
spellDifficulty: 
spellClass: Special
spellResisted: 
spellDuration: '"Permanent"'
spellCastingTime: '"1 minute to enchant the gem, 5 seconds to record a page of material."'
spellCost: "10 to enchant the gem"
spellMaintenance: "½ that to maintain"
spellPrerequisites: [Magery, Borrow Language]
spellPrereqText: Magery, Borrow Language
spellSource: Codex Arcanum
spellReference: GOCA69
spellLink: [[Codex Arcanum.pdf#page=69&search=Gem Write]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=69&search=Gem Write|Spell Link]]

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