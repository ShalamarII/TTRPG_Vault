---
tags:
  - Spell
  - SpellsAsMagic
spellID:  
spellName: Create Mana Node
spellCollege: [Meta]
spellDifficulty: 
spellClass: Enchantment
spellResisted: 
spellDuration: '"Permanent, until the nod is destroyed and forgotten."'
spellCastingTime: '"Variable"'
spellCost: "1000 per mana point of mana crystals produced per day. 500 if the mana crystals are"
spellMaintenance: ""
spellPrerequisites: [Magery 2, Restore Mana, Increase Mana, Crystallize Mana.]
spellPrereqText: Magery 2, Restore Mana, Increase Mana, Crystallize Mana.
spellSource: Codex Arcanum
spellReference: GOCA348
spellLink: [[Codex Arcanum.pdf#page=348&search=Create Mana Node]]
spellPoints: 1
spellTags: None Given
spellWeapons: 
---

 [[Codex Arcanum.pdf#page=348&search=Create Mana Node|Spell Link]]

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