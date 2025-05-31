---
date created: Saturday, January 13th 2024, 8:38:03 am
date modified: Saturday, January 13th 2024, 10:00:06 am
alias: Probability Calculator
tags: tools, dice
baseSkill: 12
maneuver: 0
sizeModifier: 0
posture: 0
range: 0
hitLocation: 0
difficulty: 0
skillLevel: 12
otherMod: 
---

> [!info]-
> **Effective Skill** = Base Skill + Maneuver + Target's Size Modifier + Postures + Range + Hit Location + Everything Else
> - **If your target is 6 or lower,** your initial chance of success is _very poor_ (9% or much lower). Bonuses greatly multiply this (tiny) chance of success, while penalties quickly eliminate it.
> - **If your target is 8**, your initial chance of success is _poor_ (25%). A +1 bonus multiplies it by 1.5 and a +2 bonus doubles it, while a -1 penalty cuts it to two-thirds and a -2 penalty cuts it to one-third.
> - **If your target is 10**, your initial chance of success is _iffy_ (50%). A +1 bonus multiplies it by 1.25 and a +2 bonus multiplies it by 1.5, while a -1 penalty cuts it to three-quarters and a -2 penalty halves it.
> - **If your target is 12**, your initial chance of success is _high_ (75%). Bonuses begin to have fairly modest effect on your chance of success, but a +1 bonus cuts your already-low chance of _failure_to two-thirds, while a +2 bonus cuts it to one-third. A -1 penalty, meanwhile, cuts your chance of _success_ to about four-fifths, while a -2 penalty cuts it to about two-thirds.
> - **If your target is 14 or higher,** your initial chance of success is _very high_ (90% and up). Bonuses have very modest effect on your chance of success, but a +1 bonus cuts your already-very-low chance of _failure_ to two-thirds, while a +2 bonus cuts it to one-third. A -1 penalty, meanwhile, cuts your chance of _success_ to about nine-tenths, while a -2 penalty cuts it to about four-fifths.

 **Base Skill Number: ** `INPUT[number:baseSkill]` **Effective Skill:** `VIEW[{baseSkill} + {maneuver} + {sizeModifier} + {posture} + {range} + {hitLocation} + {difficulty} + {otherMod}][math: skillLevel]`                                                                                                                     

**Chances of Succeeding:** `VIEW[({skillLevel}/16)]`%

| Effective Skill Calculator | Modifiers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |     |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **Maneuver**               | `INPUT[inlineSelect(option(0, Default: No mod), option(1, Aim 1 sec), option(2, Aim 2 sec), option(3, Aim 3+ sec), option(1, Evaluate +1), option(2, Evaluate +2), option(3, Evaluate +3), option(4, All-Out Attack Melee), option(1, All-Out Attack Ranged), option(2, Committed Attack Melee), option(-4, Move and Attack Melee), option(-2, Move and Attack Ranged), option(-4, Charge Attack) ):maneuver]`                                                                                                                                                                                                                               |     |
| **Size Modifier**          | `INPUT[inlineSelect(option(0, Default: 2 yards 6’), option(-10, 0.05 yard 1.8”), option(-9, 0.07 yard 2.5”), option(-8, 0.1 yard 3.5”), option(-7, 0.15 yard 5”), option(-6, 0.2 yard 7”), option(-5, 0.3 yard 10”), option(-4, 0.5 yard 18”), option(-3, 0.7 yard 2’), option(-2, 1 yard 3’), option(-1, 1.5 yards 4.5’), option(+1, 3 yards 9’), option(+2, 5 yards 15’), option(+3, 7 yards 21’), option(+4, 10 yards 30’), option(+5, 15 yards 45’), option(+6, 20 yards 60’), option(+7, 30 yards 90’), option(+8, 50 yards 150’), option(+9, 70 yards 210’), option(+10, 100 yards 300’), option(+11, 150 yards 450’) ):sizeModifier]` |     |
| **Posture**                | `INPUT[inlineSelect(option(0, Default: Standing), option(-2, Crouching – both attack and defense), option(-2, Kneeling or Sitting), option(-4, Crawling or Lying Down) ):posture]`                                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |
| **Range**                  | `INPUT[inlineSelect(option(0, Default: Close 0-5 yards), option(-3, Short 6-20 yards), option(-7, Medium 6-20 yards), option(-11, Far 101-500 yards), option(-15, Extremely Far 501+ yards) ):range]`                                                                                                                                                                                                                                                                                                                                                                                                                                        |     |
| **Hit Location**           | `INPUT[inlineSelect(option(0, Default: Chest), option(-1, Abdomen), option(-7, Skull), option(-5, Skull - Behind), option(-5, Face), option(-7, Face - Behind), option(-5, Neck), option(-2, Right Arm), option(-2, Left Arm), option(-4, Shielded Right/Left Arm), option(-2, Right Leg), option(-2, Left Leg), option(-4, Hand/Foot), option(-8, Shielded Hand) ):hitLocation]`                                                                                                                                                                                                                                                            |     |
| **General Difficulty**     | `INPUT[inlineSelect(option(0, Default: Average), option(10, Automatic), option(9, Trivial), option(7, Very Easy), option(5, Easy), option(3, Very Favorable), option(1, Favorable), option(-1, Unfavorable), option(-3, Very Unfavorable), option(-5, Hard), option(-7, Very Hard), option(-9, Dangerous) ):difficulty]`                                                                                                                                                                                                                                                                                                                     |     |
| **Other Modifier**         | `INPUT[number:otherMod]`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |     |
 
```meta-bind-button
label: Reset Calculator
hidden: false
class: ""
tooltip: Reset all values to average default
id: ""
style: destructive
actions:
  - type: updateMetadata
    bindTarget: baseSkill
    evaluate: false
    value: "10"
  - type: updateMetadata
    bindTarget: maneuver
    evaluate: false
    value: "0"
  - type: updateMetadata
    bindTarget: sizeModifier
    evaluate: false
    value: "0"
  - type: updateMetadata
    bindTarget: posture
    evaluate: false
    value: "0"
  - type: updateMetadata
    bindTarget: range
    evaluate: false
    value: "0"
  - type: updateMetadata
    bindTarget: hitLocation
    evaluate: false
    value: "0"
  - type: updateMetadata
    bindTarget: difficulty
    evaluate: false
    value: "0"
  - type: updateMetadata
    bindTarget: otherMod
    evaluate: false
    value: "0"

```
