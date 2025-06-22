---
tags:
  - Spell
  - SpellsAsMagic
spellID: pxAdqI7k6Q7_DgnuD 
spellName: Message
spellCollege: [Communication & Empathy, Sound]
spellDifficulty: IQ/H
spellClass: Regular
spellResisted: Spells that block sound
spellDuration: '"Varies"'
spellCastingTime: '"Varies"'
spellCost: "1/15 sec"
spellMaintenance: "-"
spellPrerequisites: [Seeker, Great Voice, ]
spellPrereqText: Seeker, Great Voice
spellSource: Magic
spellReference: M174
spellLink: [[Magic.pdf#page=176&search=Message]]
spellPoints: 1
spellTags: Communication & Empathy, Sound
spellWeapons: 
---

 [[Magic.pdf#page=176&search=Message|Spell Link]]

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