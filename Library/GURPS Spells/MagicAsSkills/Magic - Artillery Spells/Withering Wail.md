---
tags:
  - Spell
  - SpellsAsMagic
spellID: pNGqXnStXLG203XFB 
spellName: Withering Wail
spellCollege: [Sound]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 sec/1d"'
spellCost: "2/1d"
spellMaintenance: "undefined"
spellPrerequisites: [Great Voice, Noise, 10 Spell(s) from the Sound College, Magery4, ]
spellPrereqText: Great Voice, Noise, 10 Spell(s) from the Sound College, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS25
spellLink: [[Magic - Artillery Spells.pdf#page=25&search=Withering Wail]]
spellPoints: 1
spellTags: Artillery, Sound
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=25&search=Withering Wail|Spell Link]]

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