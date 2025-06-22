---
tags:
  - Spell
  - SpellsAsMagic
spellID: pcuQz63krR2P2qhH3 
spellName: Spider Silk
spellCollege: [Animal]
spellDifficulty: IQ/H
spellClass: Missile; Special
spellResisted: undefined
spellDuration: '"1 min"'
spellCastingTime: '"1 sec"'
spellCost: "1 per 5 yd strand; max 100 yards"
spellMaintenance: "Half"
spellPrerequisites: [Magery 1, Animal 1, 2 Spell(s) from the Animal College, ]
spellPrereqText: Magery 1, Animal 1, 2 Spell(s) from the Animal College
spellSource: Magic
spellReference: M32
spellLink: [[Magic.pdf#page=34&search=Spider Silk]]
spellPoints: 1
spellTags: Animal
spellWeapons: [{"id":"Wdm5JrotjeCf-pxDc","damage":{"type":"grapple ST 10/strand"},"accuracy":"3","defaults":[{"type":"dx","modifier":-4},{"type":"skill","name":"Innate Attack","specialization":"Beam"}],"calc":{"damage":"grapple ST 10/strand"}}]
---

 [[Magic.pdf#page=34&search=Spider Silk|Spell Link]]

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