---
tags:
  - Spell
  - SpellsAsMagic
spellID: pKir_fHgvGNhKyEoQ 
spellName: Evisceration
spellCollege: [Necromancy]
spellDifficulty: IQ/VH
spellClass: Melee
spellResisted: HT or IQ
spellDuration: '"Instant"'
spellCastingTime: '"5 sec"'
spellCost: "10"
spellMaintenance: "-"
spellPrerequisites: [Steal Vitality, Apportation, Magery 3, Necromancy 3, ]
spellPrereqText: Steal Vitality, Apportation, Magery 3, Necromancy 3
spellSource: Magic
spellReference: M154
spellLink: [[Magic.pdf#page=156&search=Evisceration]]
spellPoints: 1
spellTags: Necromancy
spellWeapons: [{"id":"w3VGWsgUcNd_ZLszY","damage":{"type":"removes vital organ"},"usage":"Grapple","reach":"C","parry":"0","defaults":[{"type":"dx"},{"type":"skill","name":"Judo"},{"type":"skill","name":"Sumo Wrestling"},{"type":"skill","name":"Wrestling"}],"calc":{"damage":"removes vital organ"}}]
---

 [[Magic.pdf#page=156&search=Evisceration|Spell Link]]

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