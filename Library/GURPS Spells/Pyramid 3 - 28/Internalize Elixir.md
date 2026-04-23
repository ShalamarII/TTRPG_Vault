---
tags:
  - Spell
  - SpellsAsMagic
spellID: pWCDRzp94kXM9Ggux 
spellName: Internalize Elixir
spellCollege: [Meta]
spellDifficulty: IQ/H
spellClass: Special
spellResisted: undefined
spellDuration: '"Permanent until elixir is used"'
spellCastingTime: '"1 min/elixir"'
spellCost: "2 per $500 or the elixir being bound"
spellMaintenance: "undefined"
spellPrerequisites: [None]
spellPrereqText: 
spellSource: Pyramid 3 - 28
spellReference: PY28:10
spellLink: [[Pyramid 3 - 28.pdf#page=10&search=Internalize Elixir]]
spellPoints: 1
spellTags: Meta
spellWeapons: 
---

 [[Pyramid 3 - 28.pdf#page=10&search=Internalize Elixir|Spell Link]]

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