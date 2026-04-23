---
tags:
  - Spell
  - SpellsAsMagic
spellID: pVUVTR44vw0htPmPr 
spellName: Cone of Corrosion
spellCollege: [Water]
spellDifficulty: IQ/VH
spellClass: Regular
spellResisted: undefined
spellDuration: '"Instantaneous"'
spellCastingTime: '"1 sec/1d-1"'
spellCost: "2/1d-1×Cone width"
spellMaintenance: "undefined"
spellPrerequisites: [Acid Jet, Magery4, ]
spellPrereqText: Acid Jet, Magery4
spellSource: Magic - Artillery Spells
spellReference: MAS27
spellLink: [[Magic - Artillery Spells.pdf#page=27&search=Cone of Corrosion]]
spellPoints: 1
spellTags: Artillery, Water
spellWeapons: 
---

 [[Magic - Artillery Spells.pdf#page=27&search=Cone of Corrosion|Spell Link]]

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