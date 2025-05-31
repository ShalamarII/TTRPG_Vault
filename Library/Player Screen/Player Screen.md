<hr>

> [!GURPSLiteInfo]- [[What is GURPS|GURPS Lite]]
> ```dataview 
>TABLE PageNum 
>FROM "Library" 
>WHERE PageNum > 0 
>SORT PageNum ASC
>```

---

> [!Combat Quick Reference]- [[Library/Player Screen/Notes/Combat Quick Ref|Combat Quick Reference]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Disclaimer|Disclaimer]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Maneuvers, Active Defenses & Options|Maneuvers, Active Defenses & Options]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Situation Modifiers (Added to Combat)|Situation Modifiers]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Hit Calculations|Hit Calculations]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Range|Range/Speed Table]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Posture Table|Posture Table]] 
>[[Library/Player Screen/Notes/Combat Quick Ref#Unified Hit Locations| Unified Hit Locations]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Knockback|Knockdown]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Knockdown|Knockback]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Critical Miss Table|Critical Miss Table]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Critical Firearm Malfunction Table|Critical Firearm Malfunction Table]] 
> [[Library/Player Screen/Notes/Combat Quick Ref#Total Surprise|Total Surprise]]
> [[Library/Player Screen/Notes/Combat Quick Ref#Partial Surprise/Initiative|Partial Surprise/Party Initiative]]

---

>[!Maneuvers]- [[Library/Player Screen/Notes/Combat Quick Ref#Maneuvers|Combat Maneuvers]]
>Types of Maneuvers: <span style="color:green">Preparation</span>, <span style="color:red">Attack</span>, <span style="color:rebeccapurple">Move</span>, <span style="color:yellow">Defend</span>, <span style="color:cyan">Mental</span>. 
May add <span style="color:orange">Special</span> and/or <span style="color:pink">Extra Effort</span> to your maneuver.
> 
> | Maneuver Name                                                                 | Description                                                                                                                                                                                                                                               | Move                     | Defense     |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------- |
| <span style="color:green">Ready</span>                                        | Ready or reload a weapon (may require multiple rounds), retrieve a belt item, drink a potion, etc.                                                                                                                                                        | Step                     | Any         |
| <span style="color:pink">^Rapid Recovery^</span>                              | Pay 1 FP to ready an unready melee weapon instantly (cannot be used to ready ammo)                                                                                                                                                                        |                          |             |
| <span style="color:green">Aim (Ranged)</span>                                 | Add the weapon’s ACC to your skill for your next Attack.  +1 for each AIM maneuver after the first (max ACC+2).   *Using any Active Defense cancels the AIM bonus.  WILL roll if injured to maintain AIM bonus.                                           | Step                     | Any*        |
| <span style="color:green">Feint (Melee) </span>                               | Quick contest of your weapon/cloak skill vs the target’s weapon/cloak/shield skill or DX.  Apply win margin next attack (subtracting from their defense).                                                                                                 | Step                     | Any         |
| <span style="color:red">Regular Attack</span>                                 | Melee or Ranged.   May step (1 yard/hex) before or after attack                                                                                                                                                                                           | Step                     | Any         |
| <span style="color:red">All Out Attack<br><br>(choose one) </span>            | Determined (Melee/Ranged): 1 attack, +4 to hit (Melee) / +1 to hit (Ranged)<br><br>Strong (Melee): 1 attack, +2 damage, or +1 per dice, whichever is larger<br><br>Double (Melee): 2 attacks<br><br>Feint (Melee): Make a Feint and then 1 Regular Attack | ½ Move<br><br>(round up) | None        |
| <span style="color:red">Charge Attack </span>                                 | Charge up to your full Move then Attack.  -4 to hit (Max Effective Skill 9)  Cannot [Retreat]                                                                                                                                                             | Move                     | Dodge/Block |
| <span style="color:rebeccapurple">Change Posture</span>                       | Prone->Crouch/Kneel->Standing.    May go from Kneel->Standing as the “Step” from another maneuver                                                                                                                                                         | None                     | Any         |
| <span style="color:rebeccapurple">Jump</span>                                 | Distance in yards/hexes is Move/2 or Jumping/4 (x2 with running start, x ½ if in combat)                                                                                                                                                                  |                          | Any         |
| <span style="color:rebeccapurple">Move<br><br>(pts equal to Base Move)</span> | Move (and face) into forward hex: 1 pt; Turn 1 hex face: 1 pt; obstruction (ally, rock, log,  etc.): +1 pt; side/back step (no face change): 2 pts.   If used < ½ pts, may end with any facing, otherwise allowed 1 final hex face change.                |                          | Any         |
| <span style="color:yellow">All-Out Defense<br><br>(choose one)</span>         | Increased: +2 to any one Active Defense until your next turn<br><br>Double: can use two different defenses against an attack, until your next turn                                                                                                        | Half                     | Any         |
| <span style="color:cyan">Concentrate</span>                                   | WILL-3 roll to maintain concentration if injured or if you used an Active Defense*                                                                                                                                                                        | Step                     | Any*        |
| <span style="color:cyan">Do Nothing</span>                                    | If you are doing nothing because you are Stunned, -4 to your Active Defense                                                                                                                                                                               | None                     | Any         |
| <span style="color:orange">Wait</span>                                        | Define a “trigger”, if it occurs perform Maneuver (“If the monster moves within range, Attack!”)                                                                                                                                                          |                          |             |

---

>[!Active Defenses]- [[Library/Player Screen/Notes/Combat Quick Ref#Active Defenses|Active Defenses]]
>From Side or Back hex: -2 (0 with Peripheral Vision);
From Back hex(if started there): -4 Dodge (-2 with Peripheral Vision or Blind Fighting roll)
>
Types of Maneuvers: <span style="color:green">Preparation</span>, <span style="color:red">Attack</span>, <span style="color:rebeccapurple">Move</span>, <span style="color:yellow">Defend</span>, <span style="color:cyan">Mental</span>. 
May add <span style="color:orange">Special</span> and/or <span style="color:pink">Extra Effort</span> to your maneuver
>
>| Name of Maneuver                          | Description                                                                                                                      |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <span style="color:yellow">Dodge</span>          | Affected by Encumbrance.  May be used multiple times per round.                                                                  |
| <span style="color:orange">Dive!</span>   | +3 to Dodge.   Only against Ranged attacks.   Posture now Prone.                                                                 |
| <span style="color:yellow">Parry</span>          | May only Parry attack from front or weapon side.  Subsequent Parries are at cumulative -4 (-2 if you are using a fencing weapon) |
| <span style="color:yellow">Block</span>          | May only Block one attack from front or shield side per round.  DB only adds to defenses when attacked from front/shield side    |
| <span style="color:orange">Retreat</span> | Step back 1 hex.  +3 Dodge/+1 Block/+1 Parry (+3 Parry w/Boxing, Judo, Karate or Fencing weapon) vs 1 Melee attack/round         |

---

>[!Additional Combat Options]- [[Library/Player Screen/Notes/Combat Quick Ref#Additional Combat Options|Additional Combat Options]]
>Types of Maneuvers: <span style="color:green">Preparation</span>, <span style="color:red">Attack</span>, <span style="color:rebeccapurple">Move</span>, <span style="color:yellow">Defend</span>, <span style="color:cyan">Mental</span>. 
May add <span style="color:orange">Special</span> and/or <span style="color:pink">Extra Effort</span> to your maneuver
>
>| Name of Option                                  | Description                                                                                                                                                                                     |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span style="color:orange">Rapid Strike</span>  | Trade only one of your attacks this round for two attacks.   Each attack is -6 to hit (-3 if Trained by a Master or Weapon Master).                                                             |
| <span style="color:pink">Flurry of Blows</span> | Halve the [Rapid Strike] penalty (round down) for 1 FP per attack.                                                                                                                              |
| <span style="color:orange">Attack Armor</span>  | Piercing (PI) and Impaling (IMP) attacks can halve (½) torso DR (round down) at -8 to hit.  -10 to hit any other location.                                                                      |
| <span style="color:orange">Sweep</span>         | Roll vs Sweep (default: melee weapon skill -3) to hit, Target may defend. <br>If hit, roll QC vs your Sweep\|ST vs ST\|DX\|Acrobatics\|or best grappling skill.  Target falls if they lose QC.  |
| <span style="color:orange">Grapple</span>       | Requirement: Attack, All out Attack or Charge Attack.  <br>Roll DX or grappling skill to hit.  If hit, target is -4 DX and can’t move away.  Can break free with QC or ST (+5 if using 2 hands) |

---

> [!Situation Modifiers DMScreen]- [[Library/Player Screen/Notes/Combat Quick Ref#Situation Modifiers (Added to Combat)|Situation Modifiers]]
> | Situation                                                | Modifier                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bad Footing                                              | -2                                                                                                                                                                                                                                                                                                             |
| Distraction (clothes on fire, etc.)                      | -2 to -4                                                                                                                                                                                                                                                                                                       |
| Cover                                                    | -2 to -4                                                                                                                                                                                                                                                                                                       |
| Darkness                                                 | -1 to -9                                                                                                                                                                                                                                                                                                       |
| Blind                                                    | -10                                                                                                                                                                                                                                                                                                            |
| Shooting behind cover                                    | -2                                                                                                                                                                                                                                                                                                             |
| Attacking an opponent in Close Combat range with another | -2                                                                                                                                                                                                                                                                                                             |
| Grappled                                                 | -4                                                                                                                                                                                                                                                                                                             |
| Holding a Large Shield                                   | -2                                                                                                                                                                                                                                                                                                             |
| Attacking from above (Melee)                             | -2                                                                                                                                                                                                                                                                                                             |
| Attacking through unfriendly hex                         | -4                                                                                                                                                                                                                                                                                                             |
| Using improvised weapon                                  | -1 to -3                                                                                                                                                                                                                                                                                                       |
| Above target (Ranged)                                    | +1                                                                                                                                                                                                                                                                                                             |
| Below target (Ranged)                                    | -1                                                                                                                                                                                                                                                                                                             |
| Close Combat (Ranged)                                    | -Bulk, etc.                                                                                                                                                                                                                                                                                                    |
| Shock                                                    | Reduce IQ and DX based skills by HP lost (max -4) for one round.   Does not affect Active Defenses or Knockback check.                                                                                                                                                                                         |
| Stunned:                                                 | Active Defenses -4.  On next turn must Do Nothing & roll vs IQ to “snap out of it”, +1 for every turn in Stun (+6 for Combat Reflexes)                                                                                                                                                                         |
| **Attacker cannot see anything**                         | If blind or in total darkness, the attacker can make a **Hearing-2** roll or use another method to locate the foe.  -  **Fail Hearing Roll**: Attack in a randomly chosen direction (specify hex on map).  -  **Attack Penalty**: -10 (or -6 if accustomed to blindness).  -  **Hit Location**: Roll randomly. |
| **Attacker cannot see foe but can see surroundings**     | If the foe is invisible but surroundings are visible, use the above rules with the following adjustments: - **Attack Penalty**: -6.                                                                                                                                                                            |
| **Attacker cannot see foe but knows exact location**     | If the foe is in a smoke-filled hex or similar obscured area: - **No Hearing Roll Required**. - **Attack Penalty**: -4.                                                                                                                                                                                        |
| **Defender cannot see attacker**                         | If the attacker (or weapon) is invisible but the defender is aware of the attack: - **Dodge Penalty**: -4. - **Hearing-2 Roll Success**: Defender may parry or block at -4. - **Completely Unaware**: No defense allowed.                                                                                      |
| **Attacker in smoke/unusual darkness, defender not**     | Defender defends **normally** since the weapon is visible.                                                                                                                                                                                                                                                     |

---

>[!Special Combat DMScreen]- Special Combat Rules

---

>[!Influence Rolls DMScreen]- Influence Rolls
>An “Influence roll” is a deliberate attempt to ensure a positive reaction from an NPC. A PC with an appropriate “Influence skill” can always elect to substitute an Influence roll for a regular reaction roll in suitable circumstances (GM’s decision). See Reaction Rolls (p. 494) for more on NPC reactions. <br><br>Decide which Influence skill you are using: Diplomacy, Fast-Talk, Intimidation, Savoir-Faire, Sex Appeal, or Streetwise. Choose wisely! The GM may allow other skills to work as Influence skills in certain situations (e.g., Law skill, when dealing with a judge). Then roll a Quick Contest: your Influence skill vs. the subject’s Will. <br><br>Modifiers: All your personal reaction modifiers (although the GM or the skill description may rule that some modifiers do not apply); any specific modifiers given in the skill description; -1 to -10 for using an inappropriate Influence skill (GM’s decision).
><h3>Psychological Warfare</h3>You can use Propaganda skill for media manipulation, and Psychology skill for other “psyops.” This is an Influence roll. Apply your cause’s reaction modifiers rather than your own, and use the average Will of the target group in the Quick Contest.
>
> >[!Influence Rolls Table DMScreen]- Influence Rolls Table
>|Outcome|Reaction|Modifier|
|---|---|---|
|Win|Good|Very Good if using Sex Appeal|
|Any other result|Bad|Very Bad if using Intimidation|
|Using Diplomacy|GM makes a regular reaction roll|Better of the two results is used|
|Target is Indomitable|Automatic Loss|Unless you have appropriate Empathy (Animal, Plant, Spirit, or Empathy)|
|Target has Unfazeable|Automatic Loss|Intimidation attempts fail|
|Target has Slave Mentality|Automatic Win|No roll required|
>

---

>[!Will Rolls DMScreen]- Will Rolls
>When you are faced with a stressful situation or a distraction, the GM may require you to roll against your Will to stay focused. On a success, you may act normally. On a failure, you submit to the fear, give in to the pressure, are distracted from your task, etc. The effects of a failed Will roll in a stressful situation are often identical to those of a failed self-control roll for a mental disadvantage. This does not make Will rolls and self-control rolls interchangeable. Which kind of roll you must make depends on the cause of the stress, not on its effects. If a game-world event causes negative effects (distraction, stunning, etc.) for anyone who fails a Will roll, you roll against Will just like anyone else – even if your self-control roll to resist identical effects from a mental disadvantage would be easier or harder. If a mental disadvantage causes a negative effect on a failed self-control roll, you roll against your self-control number to resist – even if your Will roll to avoid that same effect under other circumstances would differ. However, modifiers to self-control rolls and Will rolls to resist a particular effect are usually interchangeable. For instance, a drug that gives +2 to Will rolls to resist distraction would also give +2 to self-control rolls to resist disadvantages that result in distraction
>
> >[!Fright Rolls Table DMScreen]- Fright Rolls Table
>|Roll|Effect|
|---|---|
|4-5|Stunned for one second, then recover automatically.|
|6-7|Stunned for one second. Roll vs. unmodified Will each second afterward to recover.|
|8-9|Stunned for one second. Roll vs. modified Will each second afterward to recover.|
|10|Stunned for 1d seconds. Roll vs. modified Will each second afterward to recover.|
|11|Stunned for 2d seconds. Roll vs. modified Will each second afterward to recover.|
|12|Retching for (25 - HT) seconds, then roll vs. HT each second to recover.|
|13|Acquire a new mental quirk.|
|14-15|Lose 1d FP and stunned for 1d seconds as per roll of 10.|
|16|Stunned for 1d seconds as per roll of 10, and acquire a new quirk as per roll of 13.|
|17|Faint for 1d minutes. Roll vs. HT each minute to recover.|
|18|Faint for 1d minutes and take 1 HP injury on failed HT roll when collapsing.|
|19|Severe faint for 2d minutes. Roll vs. HT each minute to recover. Take 1 HP injury.|
|20|Faint bordering on shock for 4d minutes. Lose 1d FP.|
|21|Panic for 1d minutes. Roll vs. unmodified Will each minute to recover.|
|22|Acquire a -10-point Delusion.|
|23|Acquire a -10-point Phobia or other -10-point mental disadvantage.|
|24|Major physical effect worth -15 points of physical disadvantages.|
|25|Existing Phobia becomes worse, or acquire a new -10-point Phobia or mental disadvantage.|
|26|Faint for 1d minutes and acquire a -10-point Delusion.|
|27|Faint for 1d minutes and acquire a -10-point mental disadvantage.|
|28|Light coma, unconscious for 30 minutes. -2 to all skills for 6 hours after recovery.|
|29|Coma for 1d hours. Roll vs. HT to recover. Failure extends coma by another 1d hours.|
|30|Catatonia for 1d days. Roll vs. HT to recover. No care results in increasing HP loss per day.|
|31|Seizure lasting 1d minutes, costing 1d FP. Possible injury or permanent HT loss on failure.|
|32|Stricken, taking 2d injury due to mild heart attack or stroke.|
|33|Total panic. Random, potentially dangerous actions. Roll vs. Will to recover.|
|34|Acquire a -15-point Delusion.|
|35|Acquire a -15-point Phobia or other -15-point mental disadvantage.|
|36|Severe physical effect worth -20 points of physical disadvantages.|
|37|Severe physical effect worth -30 points of physical disadvantages.|
|38|Coma as per roll of 29, and a -15-point Delusion.|
|39|Coma as per roll of 29, and a -15-point Phobia or other -15-point mental disadvantage.|
|40+|As per roll of 39, plus permanent loss of 1 IQ point, reducing all IQ-based skills and spells.|
>

---

>[!Physical Feats DMScreen]- Physical Feats
> >[!Climbing DMScreen]- Climbing
>To climb anything more difficult than a ladder, roll against Climbing skill (p. 183). This defaults to DX-5. Modifiers to the roll depend on the difficulty of the climb (see below). In all cases, subtract your encumbrance level from your roll as well. Climbing while heavily laden is a dangerous matter! <br><br>Make one roll to start the climb and another roll every five minutes. Any failure means you fall (see Falling, p. 431). If you secured yourself with a rope, you will fall only to the end of the rope unless you rolled a critical failure. <br><br>The table below gives skill modifiers and climbing speeds for some common climbs. In most cases, use the speeds in the “Regular” column. The “Combat” column is for climbs inspired by rage or terror, which always cost at least 1 FP – or double the FP cost given in an adventure or assessed by the GM. Climbs in combat require a Move maneuver.
> > >[!Climbing Table DMScreen]- Climbing Table
>| Type of Climb             | Modifier | Combat Speed | Regular Speed |
| ------------------------- | -------- | ------------ | ------------- |
| Ladder going up           | No roll  | 1 rung/sec   | 3 rungs/sec   |
| Ladder going down         | No roll  | 1 rung/sec   | 2 rungs/sec   |
| Ordinary tree             | +5       | 1 ft/3 sec   | 1 ft/sec      |
| Ordinary mountain         | 0        | 10 ft/min    | 1 ft/2 sec    |
| Vertical stone wall       | -3       | 4 ft/min     | 1 ft/5 sec    |
| Modern building           | -3       | 2 ft/min     | 1 ft/10 sec   |
| Rope-up                   | -2       | 20 ft/min    | 1 ft/sec      |
| Rope-down (w/o equipment) | -1       | 30 ft/min    | 2 ft/sec      |
| Rope-down (w/ equipment)  | -1       | 12 ft/sec    | 12 ft/sec     |
>
> >[!Digging DMScreen]- Digging
>Digging rate depends on the type of soil, the digger’s Basic Lift (that is, ST¥ST/5), and the quality of the tools available. <br><br>Loose Soil, Sand, etc.: A man can dig 2¥BL cubic feet per hour (cf/hr). <br><br>Ordinary Soil: A man can dig BL cf/hr. One man with a pick can break up 4¥BL cf/hr, making it into loose soil, which is easier to remove. The most efficient way to dig is with one man with a pick, and two shovelers clearing behind him. <br><br>Hard Soil, Clay, etc.: Must be broken up first by a pick, at 2¥BL cf/hr, and then shoveled at 2¥BL cf/hr. A lone man with both pick and shovel can only remove 0.6¥BL cf/hr – he loses time switching between tools. <br><br>Hard Rock: Must be broken by a pick at BL cf/hr (or slower, for very hard rock!), and then shoveled at BL cf/hr. <br><br>All of the above assumes iron or steel tools! Halve speeds for wooden tools (common at TL5 and below). Divide by 4 (or more) for improvised tools – bare hands, mess kits, etc. <h3>Time Required and Fatigue Cost</h3> To find the time required to dig a given hole, find the volume of the hole in cubic feet by multiplying height ¥ width ¥ depth (all in feet). Then divide the number of cubic feet by the digging rate to find the hours of work required. Each hour of work costs 1 FP for loose soil, 2 FP for ordinary soil, 3 FP for hard soil, and 4 FP for hard rock.
> > >[!Digging Table DMScreen]- Digging Table
>|Material Type|Digging Method|Speed|Notes|
|---|---|---|---|
|Loose Soil, Sand, etc.|Shovel|2×BL cf/hr||
|Ordinary Soil|Shovel|BL cf/hr||
|Ordinary Soil|Pick + 2 Shovelers|4×BL cf/hr (pick) + 2×BL cf/hr (shovel)|Most efficient method|
|Hard Soil, Clay, etc.|Pick (break up)|2×BL cf/hr|Must be broken up before shoveling|
||Shovel|2×BL cf/hr||
||Pick + Shovel (same person)|0.6×BL cf/hr|Inefficient due to time lost switching tools|
|Hard Rock|Pick (break up)|BL cf/hr|May be slower for very hard rock|
||Shovel|BL cf/hr||
>
> >[!Holding Breath DMScreen]- Holding Your Breath
>Adventurers often need to hold their breath – whether to dive or to survive poison gas, strangulation, vacuum, etc. Your HT determines the length of time you can hold your breath, as follows:
> > >[!Holding Breath Table DMScreen]- Holding Breath Table
>|Activity Level|Duration|Notes|
|---|---|---|
|No Exertion (e.g., sitting quietly or meditating)|HT × 10 seconds||
|Mild Exertion (e.g., operating a vehicle, treading water, or walking)|HT × 4 seconds||
|Heavy Exertion (e.g., climbing, combat, or running)|HT seconds||
|**Modifiers**|||
|Deep Breath (1 second, Concentrate maneuver)|× 1 (base time)|Required for standard duration|
|Hyperventilating|× 1.5||
|Hyperventilating with Pure Oxygen|× 2.5||
|Successful Breath Control Roll|× 1.5|Stacks with other multipliers|
|No Deep Breath (e.g., surprise gas attack)|÷ 2||
|Breath-Holding Advantage (each level)|× 2 per level|Cumulative for multiple levels|
|**After Maximum Duration**|||
|Start losing FP|1 FP per second||
|At 0 FP|Will roll every second or fall unconscious|Risk of death unless rescued|
>
> >[!Jumping DMScreen]- Jumping
>When you want to jump over something with a Size Modifier 3 less than yours or smaller (which encompasses most “ordinary” obstacles), the GM should say, “Okay, you jumped over it,” and get on with play. Such jumps succeed automatically. But when the obstacle seems really significant, or if the GM put it there as a deliberate hazard, use the following table. <h3>Jumping During Combat</h3> The jumping distance formulas assume you take the time to crouch and prepare for the jump. In combat, this takes two consecutive Concentrate maneuvers. Halve all distances if you jump without such preparation. If you jump over a small obstacle during a fight (anything with a Size Modifier 3 less than yours or smaller), you must use a Move maneuver, and the jump costs one extra movement point. To jump over a larger obstruction (e.g., a chair) or onto something (e.g., a table) during a fight takes your entire turn and requires a Move maneuver. Unless the jump is extreme, the GM will assume you can make the jump. (Don’t interrupt a battle to calculate jumping distance every time somebody jumps onto a chair!) However, you must make a DX roll when you make a vertical jump or a long horizontal one. A difficult jump (into a pit, for instance) might give -1 to -5 to this DX roll. The GM determines whether you must roll, and at what penalty. On a failure, you fall. It takes two Change Posture maneuvers to stand up again. On a critical failure, you fall off the thing you jumped onto, or land badly if you were jumping down, and take normal falling damage for that height (see Falling, p. 431). To clamber onto a vertical obstacle without risking a DX roll, take two consecutive Move maneuvers. Success is automatic. <h3>Jumping Skill</h3> If you have the Jumping skill (p. 203), you may substitute half your skill level, rounded down, for Basic Move in the distance formulas. In addition, you may roll against Jumping instead of DX whenever you make a difficult jump.
> > >[!Jumping Table DMScreen]- Jumping Table
>|Type of Jump|Formula|Example (Basic Move 6)|Notes|
|---|---|---|---|
|**Standing High Jump**|(6 × Basic Move) - 10 inches|26 inches||
|**Running High Jump**|(6 × (Basic Move + Running Yards)) - 10 inches|Varies with running distance|Max height = 2 × Standing High Jump|
|**Standing Broad Jump**|(2 × Basic Move) - 3 feet|9 feet||
|**Running Broad Jump**|(2 × (Basic Move + Running Yards)) - 3 feet|Varies with running distance|Max distance = 2 × Standing Broad Jump|
>

---

>[!Senses DMScreen]- Senses
> >[!Vision DMScreen]- Vision
>Make a Vision roll whenever it is important that you see something. <br><br>Modifiers: Any Acute Vision bonus; +3 for Hyperspectral Vision; modifiers for the size and range of the target (see p. 550); -1 to -9 in partial darkness. In total darkness, Vision rolls are impossible without special advantages or technological aids. <br><br>To spot something in plain sight – e.g., a car coming toward you on the road – roll at +10. This does not apply to attempts to spot hidden objects, read text, identify faces, etc. When you try to spot something that is deliberately hidden, the GM may treat this roll as a Quick Contest against a concealment skill (Camouflage, Holdout, etc.), and may allow – or require – a skill such as Observation or Search to replace Perception for the roll. <br><br>Note that the curvature of a planet blocks vision beyond the horizon. The normal horizon on an Earthsized planet is about three miles for an observer five to six feet in height. The GM should increase this for taller observers or those in elevated positions. There is no horizon in space! <br><br>Useful Advantages: Night Vision cancels -1 in partial darkness penalties per level, and Dark Vision lets you ignore darkness penalties. Peripheral Vision gives you a Vision roll to see anything that is not absolutely, positively, directly behind you – and 360° Vision lets you see even that! Telescopic Vision cancels -1 in range penalties per level. <br><br>Limiting Disadvantages: Bad Sight gives -6 to Vision rolls to spot items more than one yard away if you are nearsighted, or items within one yard if you are farsighted. Restricted Vision prevents you from noticing anything that isn’t in the direction you are looking. Blindness means you can see nothing!
>
> >[!Hearing DMScreen]- Hearing
>Make a Hearing roll whenever it is important that you hear a sound. The GM will often require a separate IQ roll to make out speech, especially in a foreign language. <br><br>Modifiers: Any Acute Hearing bonus; +4 for Discriminatory Hearing; -4 for Hard of Hearing. The GM may make this roll easier or harder, depending on the loudness of the sound, surrounding noises, etc. <br><br>The range at which you can hear a sound at no penalty is given on the table below. For each step by which you are closer than this, apply +1 to the roll, while for each step by which you are more distant, apply -1. For instance, to hear normal conversation at 8 yards would require a roll at -3. <br><br>When you try to hear someone who is attempting to move silently, the GM may treat this roll as a Quick Contest against his Stealth skill. If you are actively listening for such activity, the GM may allow you to substitute Observation skill for Perception. <br><br><i>Useful Advantages</i>: Parabolic Hearing allows you to hear distant sounds as if they were nearby. Subsonic Hearing and Ultrahearing can detect sounds that are inaudible to normal humans. <br><br><i>Limiting Disadvantage</i>: If you suffer from Deafness, you can hear nothing!
> > >[!Hearing Table DMScreen]- Hearing Table
>|Sound|Range (yards)|
|---|---|
|Leaves rustling|¼|
|Quiet conversation|½|
|Normal conversation|1|
|Light traffic|2|
|Loud conversation|4|
|Noisy office|8|
|Normal traffic|16|
|“Quiet” rock band|32|
|Heavy traffic|64|
|Jet takeoff|128|
|Very loud rock band|256|
|Metallica|512|
>
> >[!Smell/Taste DMScreen]- Smell
>Taste and smell are two manifestations of the same sense. Make a Taste roll to notice a flavor, or a Smell roll to notice a scent. <br><br>Modifiers: Any Acute Taste and Smell bonus; +4 for Discriminatory Smell or Taste (as applicable). The GM may modify this roll for a particularly strong or weak taste or odor, and may apply a penalty if it is specifically disguised. <br><br>Useful Advantages: In addition to giving a bonus to your roll, Discriminatory Smell and Discriminatory Taste can reveal sufficient detail to allow you to identify people, locations, and objects with precision equivalent to hearing or vision for a normal human. <br><br>Limiting Disadvantage: No Sense of Smell/Taste means that you cannot taste or smell anything.

---

>[!Skills DMSheet]- [[Skills (By Category)|Skills (By Category)]]
> >[!Animal Skills]- Animal
| Skill                   | Diff | Attr | Defaults                                        | Page |
| ----------------------- | ---- | ---- | ----------------------------------------------- | ---- |
| Animal Handling†        | A    | IQ   | IQ-5                                            | B175 |
| Falconry                | A    | IQ   | IQ-5, Animal Handling (Raptors)-3               | B194 |
| Mimicry (Animal Sounds) | H    | IQ   | IQ-6*                                           | B210 |
| Mimicry (Bird Calls)    | H    | IQ   | IQ-6*                                           | B210 |
| Mount                   | A    | DX   | DX-5                                            | B210 |
| Naturalist              | H    | IQ   | IQ-6, Biology-3                                 | B211 |
| Packing                 | A    | IQ   | IQ-5, Animal Handling (Equines)-5               | B212 |
| Riding†                 | A    | DX   | DX-5, Animal Handling, Riding (same)-3          | B217 |
| Teamster†               | A    | IQ   | Animal Handling (same)-4, Riding (same)-2       | B225 |
| Veterinary/TL           | A    | IQ   | Animal Handling (any)-6, Physician-5, Surgery-5 | B228 |
>
> >[!Arts/Entertainment Skills]- Arts/Entertainment
|Skill|Diff|Attr|Defaults|Page|
|---|---|---|---|---|
|Artist†|H|IQ|IQ-6|B179|
|Connoisseur†|A|IQ|IQ-5*|B185|
|Current Affairs/TL (High Culture)|E|IQ|IQ-4, Research-4|B186|
|Current Affairs/TL (Popular Culture)|E|IQ|IQ-4, Research-4|B186|
|Dancing|A|DX|DX-5|B187|
|Electronics Operation/TL (Media)|A|IQ|IQ-5, Engineer (Electrical)-3, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Fire Eating|A|DX|None|B195|
|Group Performance†|A|IQ|IQ-5*|B198|
|Makeup/TL|E|IQ|IQ-4, Disguise-2|B206|
|Mimicry†|H|IQ|IQ-6*|B210|
|Musical Composition|H|IQ|Musical Instrument-2, Poetry-2 (for song)|B210|
|Musical Instrument†|H|IQ|Special|B211|
|Performance|A|IQ|IQ-5, Acting-2, Public Speaking-2|B212|
|Photography/TL|A|IQ|IQ-5, Electronics Operation (Media)-5|B213|
|Poetry|A|IQ|IQ-5, Writing-5|B214|
|Singing|E|HT|HT-4|B220|
|Sleight of Hand|H|DX|Filch-5|B221|
|Stage Combat|A|DX|Combat Art or Sport-2, an actual combat skill-3, Performance-3|B222|
|Ventriloquism|H|IQ|None|B228|
|Writing|A|IQ|IQ-5|B228|
>
> >[!Athletic Skills]- Athletic
>| Skill          | Diff   | Attr | Defaults                     | Page |
| -------------- | ------ | ---- | ---------------------------- | ---- |
| Acrobatics     | H      | DX   | DX-6                         | B174 |
| Aerobatics     | H      | DX   | DX-6                         | B174 |
| Aquabatics     | H      | DX   | DX-6                         | B174 |
| Bicycling      | E      | DX   | DX-4, Driving (Motorcycle)-4 | B180 |
| Body Sense     | H      | DX   | DX-6, Acrobatics-3           | B181 |
| Breath Control | H      | HT   | None                         | B182 |
| Climbing       | A      | DX   | DX-5                         | B183 |
| Combat Art†    | Varies | DX   | Special                      | B184 |
| Flight         | A      | HT   | HT-5                         | B195 |
| Free Fall      | A      | DX   | DX-5, HT-5                   | B197 |
| Hiking         | A      | HT   | HT-5                         | B200 |
| Jumping        | E      | DX   | None                         | B203 |
| Lifting        | A      | HT   | None                         | B205 |
| Mount          | A      | DX   | DX-5                         | B210 |
| Parachuting/TL | E      | DX   | DX-4                         | B212 |
| Running        | A      | HT   | HT-5                         | B218 |
| Scuba/TL       | A      | IQ   | IQ-5, Diving Suit-2          | B219 |
| Sports†        | A      | DX   | Special                      | B222 |
| Swimming       | E      | HT   | HT-4                         | B224 |
| Throwing       | A      | DX   | DX-3, Dropping-4             | B226 |
>
> >[!Business Skills]- Business
>|Skill|Diff|Attr|Defaults|Page|
|---|---|---|---|---|
|Accounting|H|IQ|IQ-6, Finance-4, Mathematics (Statistics)-5, Merchant-5|B174|
|Administration|A|IQ|IQ-5, Merchant-3|B174|
|Current Affairs/TL (Business)|E|IQ|IQ-4, Research-4|B186|
|Diplomacy|H|IQ|IQ-6, Politics-6|B187|
|Economics|H|IQ|IQ-6, Finance-3, Market Analysis-5, Merchant-6|B189|
|Finance|H|IQ|Accounting-4, Economics-3, Merchant-6|B195|
|Law†|H|IQ|IQ-6|B204|
|Market Analysis|H|IQ|IQ-6, Economics-5, Merchant-4|B207|
|Mathematics/TL (Statistics)|H|IQ|IQ-6*|B207|
|Merchant|A|IQ|IQ-5, Finance-6, Market Analysis-4|B209|
|Politics|A|IQ|IQ-5, Diplomacy-5|B215|
|Public Speaking|A|IQ|IQ-5, Acting-5, Performance-2, Politics-5|B216|
|Savoir-Faire (High Society)|E|IQ|IQ-4 and others|B218|
>
> >[!Combat/Weapon Skills]- Combat/Weapon
>|Skill|Diff|Attr|Defaults|Page|
|---|---|---|---|---|
|Axe/Mace|A|DX|Flail-4, Two-Handed Axe/Mace-3|B208|
|Boxing|A|DX|None|B182|
|Brawling|E|DX|None|B182|
|Broadsword|A|DX|Force Sword-4, Rapier-4, Saber-4, Shortsword-2, Two-Handed Sword-4|B208|
|Cloak|A|DX|DX-5, Net-4, Shield (any)-4|B184|
|Fast Draw†|E|DX|None|B194|
|Flail|H|DX|Axe/Mace-4, Two-Handed Flail-3|B208|
|Force Sword|A|DX|Any Sword-3|B208|
|Force Whip|A|DX|Kusari-3, Monowire Whip-3, Whip-3|B209|
|Garrote|E|DX|DX-4|B197|
|Jitte/Sai|A|DX|Force Sword-4, Main-Gauche-4, Shortsword-3|B208|
|Judo|H|DX|None|B203|
|Karate|H|DX|None|B203|
|Knife|E|DX|Force Sword-3, Main-Gauche-3, Shortsword-3|B208|
|Kusari|H|DX|Force Whip-3, Monowire Whip-3, Two-Handed Flail-4, Whip-3|B203|
|Lance|A|DX|DX-5, Spear-3|B204|
|Main-Gauche|A|DX|Jitte/Sai-4, Knife-4, Rapier-3, Saber-3, Smallsword-3|B208|
|Melee Weapon|Varies|DX|Special|B208|
|Monowire Whip|H|DX|Force Whip-3, Kusari-3, Whip-3|B209|
|Parry Missile Weapons|H|DX|None|B212|
|Polearm|A|DX|Spear-4, Staff-4, Two-Handed Axe/Mace-4|B208|
|Rapier|A|DX|Broadsword-4, Main-Gauche-3, Saber-3, Smallsword-3|B208|
|Saber|A|DX|Broadsword-4, Main-Gauche-3, Rapier-3, Shortsword-4, Smallsword-3|B208|
|Shield†|E|DX|DX-4|B220|
|Shortsword|A|DX|Broadsword-2, Force Sword-4, Jitte/Sai-3, Knife-4, Saber-4, Smallsword-4, Tonfa-3|B209|
|Smallsword|A|DX|Main-Gauche-3, Rapier-3, Saber-3, Shortsword-4|B208|
|Spear|A|DX|Polearm-4, Staff-2|B208|
|Staff|A|DX|Polearm-4, Spear-2|B208|
|Sumo Wrestling|A|DX|None|B223|
|Tonfa|A|DX|Shortsword-3|B209|
|Two-Handed Axe/Mace|A|DX|Axe/Mace-3, Polearm-4, Two-Handed Flail-4|B208|
|Two-Handed Flail|H|DX|Flail-3, Kusari-4, Two-Handed Axe/Mace-4|B208|
|Two-Handed Sword|A|DX|Broadsword-4, Force Sword-4|B209|
|Whip|A|DX|Force Whip-3, Kusari-3, Monowire Whip-3|B209|
|Wrestling|A|DX|None|B228|
>
> >[!Ranged Combat Skills]- Ranged Combat Skills
>|Skill|Diff|Attr|Defaults|Page|
|---|---|---|---|---|
|Artillery/TL†|A|IQ|IQ-5|B178|
|Beam Weapons/TL†|E|DX|DX-4|B179|
|Blowpipe|H|DX|DX-6|B180|
|Bolas|A|DX|None|B182|
|Bow|A|DX|DX-5|B182|
|Crossbow|E|DX|DX-4|B186|
|Dropping|A|DX|DX-3, Throwing-4|B189|
|Fast-Draw†|E|DX|None|B194|
|Gunner/TL†|E|DX|DX-4|B198|
|Guns/TL†|E|DX|DX-4|B198|
|Innate Attack†|E|DX|DX-4|B201|
|Lasso|A|DX|None|B204|
|Liquid Projector/TL†|E|DX|DX-4|B205|
|Net|H|DX|Cloak-5|B211|
|Sling|H|DX|DX-6|B221|
|Spear Thrower|A|DX|DX-5, Thrown Weapon (Spear)-4|B222|
|Throwing Art|H|DX|None|B226|
|Thrown Weapon†|E|DX|DX-4*|B226|
>
> >[!Craft Skills]- Craft
>|Skill|Diff|Attr|Defaults|Page|
| ---                  | --- | --- | ---                                            | ---                     |
| -------------------- | --- | --- | ---------------------------------------------- | ----------------------- |
| Artist (Pottery)     | H   | IQ  | IQ-6                                           | B179                    |
| Artist (Sculpting)   | H   | IQ  | IQ-6                                           | B179                    |
| Artist (Woodworking) | H   | IQ  | IQ-6                                           | B179                    |
| Bone Carving         | A   | DX  | DX-2, Armoury (TL0)-2                          | Lands Out of Time pg 11 |
| Carpentry            | E   | IQ  | IQ-4                                           | B183                    |
| Jeweler/TL           | H   | IQ  | IQ-6, Smith (Copper)-4, Smith (Lead and Tin)-4 | B203                    |
| Leatherworking       | E   | DX  | DX-4                                           | B205                    |
| Masonry              | E   | IQ  | IQ-4                                           | B207                    |
| Smith/TL†            | A   | IQ  | IQ-5*                                          | B221                    |
>
> >[!Criminal/Street Skills]- Criminal/Street
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Carousing|E|HT|HT-4|B183|
|Climbing|A|DX|DX-5|B183|
|Computer Hacking/TL|VH|IQ|None|B184|
|Counterfeiting/TL|H|IQ|IQ-6, Forgery-2|B185|
|Disguise/TL†|A|IQ|IQ-5, Makeup-3|B187|
|Electronics Operation/TL (Security)|A|IQ|IQ-5, Engineer (Electrical)-3, Engineer (Electronics)-5|B189|
|Escape|H|DX|DX-6|B192|
|Explosives/TL (Demolition)|A|IQ|IQ-5*|B194|
|Fast-Talk|A|IQ|IQ-5, Acting-5|B195|
|Filch|A|DX|DX-5, Pickpocket-4, Sleight of Hand-4|B195|
|Forced Entry|E|DX|None|B196|
|Forgery/TL|H|IQ|IQ-6, Counterfeiting-2|B196|
|Gambling|A|IQ|IQ-5, Mathematics (Statistics)-5|B197|
|Holdout|A|IQ|IQ-5, Sleight of Hand-3|B200|
|Intimidation|A|Will|Will-5, Acting-3|B202|
|Lockpicking/TL|A|IQ|IQ-5|B206|
|Observation|A|Per|Per-5, Shadowing-5|B211|
|Panhandling|E|IQ|IQ-4, Fast Talk-2, Public Speaking-3|B212|
|Pickpocket|H|DX|DX-6, Filch-5, Sleight of Hand-4|B213|
|Poisons/TL|H|IQ|IQ-6, Chemistry-5, Pharmacy (any)-3, Physician-3|B214|
|Savoir-Faire (Mafia)|E|IQ|IQ-4 and others|B218|
|Scrounging|E|Per|Per-4|B218|
|Shadowing|A|IQ|IQ-5, Observation-5, Stealth-4 (on foot only)|B219|
|Sleight of Hand|H|DX|Filch-5|B221|
|Smuggling|A|IQ|IQ-5|B221|
|Stealth|A|DX|DX-5, IQ-5|B222|
|Streetwise|A|IQ|IQ-5|B223|
|Traps/TL|A|IQ|IQ-5, Lockpicking-3|B226|
|Urban Survival|A|Per|Per-5|B228|
>
> >[!Design/Invention Skills]- Design/Invention
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Architecture/TL|A|IQ|IQ-5, Engineer (Civil)-4|B176|
|Bioengineering/TL†|H|IQ|Biology-5|B180|
|Computer Programming/TL|H|IQ|None|B184|
|Engineer/TL†|H|IQ|Special|B190|
|Pharmacy/TL†|H|IQ|IQ-6*|B213|
|Weird Science|VH|IQ|None|B228|
>
> >[!Esoteric Skills]- Esoteric
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Autohypnosis|H|Will|Meditation-4|B179|
|Blind Fighting|VH|Per|None|B180|
|Body Control|VH|HT|None|B181|
|Breaking Blow|H|IQ|None|B182|
|Captivate|H|Will|None|B191|
|Dreaming|H|Will|Will-6|B188|
|Enthrallment†|H|Will|None|B191|
|Flying Leap|H|IQ|None|B196|
|Immovable Stance|H|DX|None|B201|
|Invisibility Art|VH|IQ|None|B202|
|Kiai|H|HT|None|B203|
|Light Walk|H|DX|None|B205|
|Meditation|H|Will|Will-6, Autohypnosis-4|B207|
|Mental Strength|E|Will|None|B209|
|Mind Block|A|Will|Will-5, Meditation-5|B210|
|Musical Influence|VH|IQ|None|B210|
|Persuade|H|Will|None|B191|
|Power Blow|H|Will|None|B215|
|Pressure Points|H|IQ|None|B215|
|Pressure Secrets|VH|IQ|None|B215|
|Push|H|DX|None|B216|
|Suggest|H|Will|None|B191|
|Sway Emotions|H|Will|None|B192|
|Throwing Art|H|DX|None|B226|
|Zen Archery|VH|IQ|None|B228|
>
> >[!Everyman Skills]- Everyman
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Area Knowledge†|E|IQ|IQ-4, Geography, (Regional)-3*|B176|
|Computer Operation/TL|E|IQ|IQ-4|B184|
|Cooking|A|IQ|IQ-5, Housekeeping-5|B185|
|Housekeeping|E|IQ|IQ-4|B200|
|Knot-Tying|E|DX|DX-4, Climbing-4, Seamanship-4|B203|
|Savoir-Faire (Servant)|E|IQ|IQ-4 and others|B218|
|Sewing/TL|E|DX|DX-4|B219|
|Typing|E|DX|DX-4, any skill requiring typing-3|B228|
|Weather Sense|A|IQ|IQ-5|B209|
>
> >[!Knowledge Skills]- Knowledge
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Area Knowledge†|E|IQ|IQ-4, Geography, (Regional)-3*|B176|
|Connoisseur†|A|IQ|IQ-5*|B185|
|Current Affairs/TL†|E|IQ|IQ-4, Research-4|B186|
|Games†|E|IQ|IQ-4|B197|
|Heraldry|A|IQ|IQ-5, Savoir-Faire (High Society)-3|B199|
|Hidden Lore†|A|IQ|None|B199|
|Hobby Skill†|E|DX or IQ|DX-4 or IQ-4|B200|
|Professional Skill†|A|DX or IQ|Special|B215|
|Savoir-Faire†|E|IQ|IQ-4 and others|B218|
>
> >[!Medical Skills]- Medical
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Diagnosis/TL|H|IQ|IQ-6, First Aid-8, Physician-4, Veterinary-5|B187|
|Electronics Operation/TL (Medical)|A|IQ|IQ-5, Engineer (Electrical)-3, IQ-5, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Esoteric Medicine|H|Per|Per-6|B192|
|Expert Skill (Epidemiology)|H|IQ|None|B193|
|First Aid/TL|E|IQ|IQ-4, Esoteric Medicine, Physician, Veterinary-4|B195|
|Hypnotism|H|IQ|None|B201|
|Pharmacy/TL†|H|IQ|IQ-6*|B213|
|Physician/TL|H|IQ|IQ-7, First Aid-11, Veterinary-5|B213|
|Poisons/TL|H|IQ|IQ-6, Chemistry-5, Pharmacy (any)-3, Physician-3|B214|
|Psychology|H|IQ|IQ-6, Sociology-4|B216|
|Surgery/TL|VH|IQ|First Aid-12, Physician-5, Physiology-8, Veterinary-5|B223|
|Veterinary/TL|H|IQ|Animal Handling (any)-6, Physician-5, Surgery-5|B228|
>
> >[!Military Skills]- Military
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Armoury/TL†|A|IQ|IQ-5, Engineer (same)-4|B178|
|Brain Hacking/TL|H|IQ|Special|B182|
|Brainwashing/TL|H|IQ|Special|B182|
|Camouflage|E|IQ|IQ-4, Survival-2|B183|
|Cryptography/TL|H|IQ|Mathematics (Cryptology)-5|B186|
|Electronics Operation/TL (Electronic Warfare)|A|IQ|IQ-5, Engineer (Electrical)-3, IQ-5, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Electronics Repair/TL (Electronic Warfare)|A|IQ|IQ-5, Electronics Operation (same)-3, Engineer (Electronics)-3|B190|
|Expert Skill (Military Science)|H|IQ|None|B193|
|Explosives/TL†|A|IQ|IQ-5*|B194|
|Forward Observer/TL|A|IQ|IQ-5, Artillery (any)-5*|B196|
|Intelligence Analysis|H|IQ|IQ-6, Strategy (any)-6|B201|
|Interrogation|A|IQ|IQ-5, Intimidation-3, Psychology-4|B202|
|Leadership|A|IQ|IQ-5|B204|
|NBC Suit/TL|A|DX|Battlesuit-2, Diving Suit-4, Vacc Suit-2|B192|
|Observation|A|Per|Per-5, Shadowing-5|B211|
|Parachuting/TL|E|DX|DX-4|B212|
|Propaganda/TL|A|IQ|IQ-5, Merchant-5, Psychology-4|B216|
|Savoir-Faire (Military)|E|IQ|IQ-4 and others|B218|
|Scuba/TL|A|IQ|IQ-5, Diving Suit-2|B219|
|Soldier/TL|A|IQ|IQ-5|B221|
|Strategy†|H|IQ|IQ-6, Intelligence Analysis-6, Tactics-6|B222|
|Tactics|H|IQ|IQ-6, Strategy (any)-6|B224|
|Traps/TL|A|IQ|IQ-5, Lockpicking-3|B226|
>
> >[!Natural Sciences Skills]- Natural Sciences
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Alchemy/TL|VH|IQ|None|B174|
|Astronomy/TL|H|IQ|IQ-6|B179|
|Biology/TL†|VH|IQ|IQ-6, Naturalist-6|B180|
|Chemistry/TL|H|IQ|IQ-6, Alchemy-3|B183|
|Expert Skill (Epidemiology)|H|IQ|None|B193|
|Expert Skill (Hydrology)|H|IQ|None|B193|
|Expert Skill (Natural Philosophy)|H|IQ|None|B193|
|Geology/TL†|H|IQ|IQ-6, Geography (Physical)-4, Prospecting-5|B198|
|Mathematics/TL†|H|IQ|IQ-6*|B207|
|Metallurgy/TL|H|IQ|Chemistry-5, Jeweler-8, Smith (any)-8|B209|
|Meteorology/TL†|A|IQ|IQ-5|B209|
|Naturalist|H|IQ|IQ-6, Biology-3|B211|
|Paleontology/TL†|H|IQ|Biology-4*|B212|
|Physics/TL|VH|IQ|IQ-6|B213|
|Physiology/TL†|H|IQ|IQ-6, Diagnosis-5, Physician-5, Surgery-5|B213|
>
> >[!Occult/Magical Skills]- Occult/Magical
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Alchemy/TL|VH|IQ|None|B174|
|Exorcism|H|Will|Will-6, Religious Ritual (any)-3, Ritual Magic (any)-3, Theology (any)-3|B193|
|Expert Skill (Psionics)|H|IQ|None|B193|
|Herb Lore/TL|VH|IQ|None|B199|
|Hidden Lore (Demon Lore)|A|IQ|None|B199|
|Hidden Lore (Faerie Lore)|A|IQ|None|B199|
|Hidden Lore (Spirit Lore)|A|IQ|None|B199|
|Occultism|A|IQ|IQ-5|B212|
|Religious Ritual†|H|IQ|Ritual Magic (same)-6, Theology (same)-4|B217|
|Ritual Magic†|VH|IQ|Religious Ritual (same)-6|B218|
|Symbol Drawing†|H|IQ|Special|B224|
|Thaumatology|VH|IQ|IQ-7 (magical settings only)|B225|
>
> >[!Outdoor/Exploration Skills]- Outdoor/Exploration
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Camouflage|E|IQ|IQ-4, Survival-2|B183|
|Cartography/TL|A|IQ|IQ-5, Geography (any)-2, Mathematics (Surveying)-2, Navigation (any)-4|B183|
|Climbing|E|DX|DX-5|B183|
|Fishing|E|Per|Per-4|B195|
|Hiking|A|HT|HT-5|B200|
|Mimicry (Animal Sounds)|H|IQ|IQ-6*|B210|
|Mimicry (Bird Calls)|H|IQ|IQ-6*|B210|
|Naturalist|H|IQ|IQ-6, Biology-3|B211|
|Navigation/TL†|A|IQ|Special|B211|
|Prospecting/TL|A|IQ|IQ-5, Geology (any)-4|B216|
|Scuba/TL|A|IQ|IQ-5, Diving Suit-2|B219|
|Skating|H|HT|HT-6|B220|
|Skiing|H|HT|HT-6|B221|
|Survival†|A|Per|Per-5, Naturalist (same planet)-3|B223|
|Swimming|E|HT|HT-4|B224|
|Tracking|A|Per|Per-5, Naturalist-5|B226|
|Weather Sense|A|IQ|IQ-5|B209|
>
> >[!Plant Skills]- Plant
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Biology/TL†|VH|IQ|IQ-6, Naturalist-6|B180|
|Farming/TL|A|IQ|IQ-5, Biology-5, Gardening-3|B194|
|Gardening|E|IQ|IQ-4, Farming-3|B197|
|Herb Lore/TL|VH|IQ|None|B199|
|Naturalist|H|IQ|IQ-6, Biology-3|B211|
|Paleontology/TL (Paleobotany)|H|IQ|Biology-4*|B212|
|Pharmacy/TL (Herbal)|H|IQ|IQ-6*|B213|
>
> >[!Police Skills]- Police
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Body Language|A|Per|Detect Lies-4, Psychology-4|B181|
|Criminology/TL|A|IQ|IQ-5, Psychology-4|B186|
|Detect Lies|H|Per|Per-6, Body Language-4, Psychology-4|B187|
|Diplomacy|H|IQ|IQ-6, Politics-6|B187|
|Electronics Operation/TL (Surveillance)|A|IQ|IQ-5, Engineer (Electrical)-3, IQ-5, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Explosives/TL (Explosive Ordnance Disposal)|A|IQ|IQ-5*|B194|
|Forced Entry|E|DX|None|B196|
|Forensics/TL|H|IQ|IQ-6, Criminology-4|B196|
|Intelligence Analysis|H|IQ|IQ-6, Strategy (any)-6|B201|
|Interrogation|A|IQ|IQ-5, Intimidation-3, Psychology-4|B202|
|Intimidation|A|Will|Defaults: Will-5 or Acting-3|B202|
|Law†|H|IQ|IQ-6|B204|
|Lockpicking/TL|A|IQ|IQ-5|B206|
|Observation|A|Per|Per-5, Shadowing-5|B211|
|Savoir-Faire (Police)|E|IQ|IQ-4 and others|B218|
|Search|A|Per|Per-5, Criminology-5|B219|
|Shadowing|A|IQ|IQ-5, Observation-5, Stealth-4 (on foot only)|B219|
|Stealth|A|DX|DX-5, IQ-5|B222|
|Streetwise|A|IQ|IQ-5|B223|
|Tactics|A|IQ|IQ-6, Strategy (any)-6|B224|
|Urban Survival|A|Per|Per-5|B228|
>
> >[!Repair/Maintenance Skills]- Repair/Maintenance
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Armoury/TL†|A|IQ|IQ-5, Engineer (same)-4|B178|
|Electrician/TL|A|IQ|IQ-5, Engineer (Electrical)-3|B189|
|Electronics Repair/TL†|A|IQ|IQ-5, Electronics Operation (same)-3, Engineer (Electronics)-3|B190|
|Flint Knapping|A|DX|DX-2, Armoury (TL0)-1, Anthropology-4|GURPS Lands Out of Time pg 11|
|Machinist/TL|A|IQ|IQ-5, Mechanic (any)-5|B206|
|Mechanic/TL†|A|IQ|IQ-5, Engineer (same)-4, Machinist-5|B207|
>
> >[!Scholarly Skills]- Scholarly
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Computer Operation/TL|E|IQ|IQ-4|B184|
|Expert Skill†|H|IQ|None|B193|
|Literature|H|IQ|IQ-6|B205|
|Public Speaking|A|IQ|IQ-5, Acting-5, Performance-2, Politics-5|B216|
|Research/TL|A|IQ|IQ-5, Writing-3|B217|
|Speed-Reading|A|IQ|None|B222|
|Teaching|A|IQ|IQ-5|B224|
|Typing|E|DX|DX-4, any skill requiring typing-3|B228|
|Writing|A|IQ|IQ-5|B228|
>
> >[!Social Skills]- Social
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Acting|A|IQ|IQ-5, Performance-2, Public Speaking-5|B174|
|Administration|A|IQ|IQ-5, Merchant-3|B174|
|Body Language|A|Per|Detect Lies-4, Psychology-4|B181|
|Carousing|E|HT|HT-4|B183|
|Connoisseur†|A|IQ|IQ-5*|B185|
|Current Affairs/TL†|E|IQ|IQ-4, Research-4|B186|
|Detect Lies|H|Per|Per-6, Body Language-4, Psychology-4|B187|
|Diplomacy|H|IQ|IQ-6, Politics-6|B187|
|Erotic Art|A|DX|DX-5, Acrobatics-5|B192|
|Fast-Talk|A|IQ|IQ-5, Acting-5|B195|
|Fortune Telling†|A|IQ|IQ-5, Fast-Talk-3, Occultism-3|B196|
|Gambling|A|IQ|IQ-5, Mathematics (Statistics)-5|B197|
|Intimidation|A|Will|Defaults: Will-5 or Acting-3|B202|
|Gesture|E|IQ|IQ-4|B198|
|Heraldry|A|IQ|IQ-5, Savoir-Faire (High Society)-3|B199|
|Leadership|A|IQ|IQ-5|B204|
|Merchant|A|IQ|IQ-5, Finance-6, Market Analysis-4|B209|
|Panhandling|E|IQ|IQ-4, Fast Talk-2, Public Speaking-3|B212|
|Politics|A|IQ|IQ-5, Diplomacy-5|B215|
|Propaganda/TL|A|IQ|IQ-5, Merchant-5, Psychology-4|B216|
|Public Speaking|A|IQ|IQ-5, Acting-5, Performance-2, Politics-5|B216|
|Savoir-Faire (High Society)|E|IQ|IQ-4 and others|B218|
|Sex Appeal|A|HT|HT-3|B219|
|Streetwise|A|IQ|IQ-5|B223|
|Teaching|A|IQ|IQ-5|B224|
>
> >[!Social Sciences/Humanities Skills]- Social Sciences/Humanities
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Anthropology†|H|IQ|IQ-6, Paleontology (Paleoanthropology)-2, Sociology-3|B175|
|Archaeology|H|IQ|IQ-6|B176|
|Cartography/TL|A|IQ|IQ-5, Geography (any)-2, Mathematics (Surveying)-2, Navigation (any)-4|B183|
|Criminology/TL|A|IQ|IQ-5, Psychology-4|B186|
|Economics|H|IQ|IQ-6, Finance-3, Market Analysis-5, Merchant-6|B189|
|Expert Skill (Egyptology)|H|IQ|None|B193|
|Expert Skill (Political Science)|H|IQ|None|B193|
|Expert Skill (Thanatology)|H|IQ|None|B193|
|Expert Skill (Xenology)|H|IQ|None|B193|
|Geography/TL†|H|IQ|IQ-6*|B198|
|History†|H|IQ|IQ-6|B200|
|Law†|H|IQ|IQ-6|B204|
|Linguistics|H|IQ|None|B205|
|Literature|H|IQ|IQ-6|B205|
|Paleontology/TL (Paleoanthropology)|H|IQ|Biology-4*|B212|
|Philosophy†|H|IQ|IQ-6|B213|
|Psychology|H|IQ|IQ-6, Sociology-4|B216|
|Sociology|H|IQ|IQ-6, Anthropology-3, Psychology-4|B221|
|Theology†|H|IQ|IQ-6, Religious Ritual (same)-4|B226|
>
> >[!Spy Skills]- Spy
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Acting|A|IQ|IQ-5, Performance-2, Public Speaking-5|B174|
|Body Language|A|Per|Detect Lies-4, Psychology-4|B181|
|Brain Hacking/TL|H|IQ|Special|B182|
|Brainwashing/TL|H|IQ|Special|B182|
|Computer Hacking/TL|VH|IQ|None|B184|
|Cryptography/TL|H|IQ|Mathematics (Cryptology)-5|B186|
|Detect Lies|H|Per|Per-6, Body Language-4, Psychology-4|B187|
|Disguise/TL†|A|IQ|IQ-5, Makeup-3|B187|
|Electronics Operation (Electronic Warfare)/TL|A|IQ|IQ-5, Engineer (Electrical)-3, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Electronics Operation (Security)/TL|A|IQ|IQ-5, Engineer (Electrical)-3, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Electronics Operation (Surveillance)/TL|A|IQ|IQ-5, Engineer (Electrical)-3, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Escape|H|DX|DX-6|B192|
|Expert Skill (Computer Security)|H|IQ|None|B193|
|Fast-Talk|A|IQ|IQ-5, Acting-5|B195|
|Filch|A|DX|DX-5, Pickpocket-4, Sleight of Hand-4|B195|
|Forced Entry|E|DX|None|B196|
|Forgery/TL|H|IQ|IQ-6, Counterfeiting-2|B196|
|Holdout|A|IQ|IQ-5, Sleight of Hand-3|B200|
|Intelligence Analysis|H|IQ|IQ-6, Strategy (any)-6|B201|
|Interrogation|A|IQ|IQ-5, Intimidation-3, Psychology-4|B202|
|Lip Reading|A|Per|Per-10|B205|
|Lockpicking/TL|A|IQ|IQ-5|B206|
|Observation|A|Per|Per-5, Shadowing-5|B211|
|Photography/TL|A|IQ|IQ-5, Electronics Operation (Media)-5|B213|
|Poisons/TL|H|IQ|IQ-6, Chemistry-5, Pharmacy (any)-3, Physician-3|B214|
|Propaganda/TL|A|IQ|IQ-5, Merchant-5, Psychology-4|B216|
|Research/TL|A|IQ|IQ-5, Writing-3|B217|
|Search|A|Per|Per-5, Criminology-5|B219|
|Shadowing|A|IQ|IQ-5, Observation-5, Stealth-4 (on foot only)|B219|
|Smuggling|A|IQ|IQ-5|B221|
|Stealth|A|DX|DX-5, IQ-5|B222|
>
> >[!Technical Skills]- Technical
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Battlesuit/TL|A|DX|DX-5, Diving Suit-4, NBC Suit-2, Vacc Suit-2|B192|
|Computer Operation/TL|E|IQ|IQ-4|B184|
|Diving Suit/TL|A|DX|DX-5, Battlesuit-4, NBC Suit-4, Scuba-2, Vacc Suit-4|B192|
|Electronics Operation/TL†|A|IQ|IQ-5, Engineer (Electrical)-3, Electronics Repair (same)-5, Engineer (Electronics)-5|B189|
|Explosives/TL†|A|IQ|IQ-5*|B194|
|Freight Handling/TL|A|IQ|IQ-5|B197|
|Hazardous Materials/TL†|A|IQ|IQ-5|B199|
|Lockpicking/TL|A|IQ|IQ-5|B206|
|Mathematics/TL (Surveying)|H|IQ|IQ-6*|B207|
|Navigation/TL†|A|IQ|Special|B211|
|Parachuting/TL|E|DX|DX-4|B212|
|Photography/TL|A|IQ|IQ-5, Electronics Operation (Media)-5|B213|
|Scuba/TL|A|IQ|IQ-5, Diving Suit-2|B219|
|Vacc Suit/TL|A|DX|DX-5, Battlesuit-2, Diving Suit-4, NBC Suit-2|B192|
>
> >[!Vehicle Skills]- Vehicle
>|Skill|Difficulty|Attribute|Defaults|Page|
|---|---|---|---|---|
|Airshipman/TL|E|IQ|IQ-4|B185|
|Battlesuit/TL|A|DX|DX-5, Diving Suit-4, NBC Suit-2, Vacc Suit-2|B192|
|Bicycling|E|DX|DX-4, Driving (Motorcycle)-4|B180|
|Boating/TL†|A|DX|DX-5, IQ-5|B180|
|Crewman/TL|E|IQ|IQ-4|B185|
|Driving/TL†|A|DX|DX-5, IQ-5|B188|
|Freight Handling/TL|A|IQ|IQ-5|B197|
|Piloting/TL†|A|DX|IQ-6|B214|
|Seamanship/TL|E|IQ|IQ-4|B185|
|Shiphandling/TL†|H|IQ|IQ-6*|B220|
|Spacer/TL|E|IQ|IQ-4|B185|
|Submarine/TL†|A|DX|IQ-6|B223|
|Submariner|E|IQ|IQ-4|B185|
|Teamster†|A|IQ|Animal Handling (same)-4, Riding (same)-2|B225|

---

>[!Study DMScreen]- Study
>Study is the mechanic by which skills (and some advantages) are added or improved by putting in the time. "Improvement through study does _not_ depend on earning bonus points."
>
>- Time: 200 hours of learning = one point in a skill
>- On the [Job Training](https://gurps.fandom.com/wiki/Job_Training "Job Training"): four hours on the job = one hour of learning. So 800 working hours = one point in a skill or about two to three points in a year.
>- Self-Teaching: Two hours of reading, exercises, practice, etc. _without an instructor_ = one hour of learning.
>- Education: one hour of instruction by a professional teacher (skill 12+ in relevant skill) = one hour of learning. To actually count the teacher must be _above_ your current skill level
>    - College semester (21 weeks) of classroom study = around one point/ subject (assumes eight hours per day maximum)
>    - full-time student can study up to five subjects per semester.
>    - A night school semester = one point in one subject
>- Intensive Training: Education requirement _and_ have more points in the skill being taught than you do. Generally limited to the military and one must have _effective_ HT 12+ to avoid “washing out”. It can last as long as 16 hours per day.
>- Adventuring: Per GM ruling can count as Intensive Training even if no teacher is present.

---

>[!Traveling DMScreen]- [[GURPS 4th - Wilderness Adventures.pdf#page=20|Traveling/Resting]]
> >[!Foraging DMScreen]- [[GURPS 4th - Wilderness Adventures.pdf#page=42|Foraging]]
>In hospitable terrain, you can supplement your supplies by foraging for food. On any day, each character can “forage” as the party travels. A successful Survival or Naturalist roll collects enough edible plants and berries for one meal. (On a 17, you poisoned yourself. Roll vs. HT. On a success, you lose 1 HP; otherwise, lose 1d HP. On an 18, you shared with your friends: the whole party suffers – each PC rolls independently.) <br><br>In suitable terrain, a successful skill roll with a missile weapon (at -4) bags a rabbit or similar creature, providing meat for two meals. Near water or at sea, a successful Fishing roll has similar results. <br><br>Each forager gets one Survival or Naturalist roll and one missile or Fishing roll per day. <br><br>Alternatively, the party can take some time off from travel and do some serious foraging. Each character can make five Survival or Naturalist rolls and five missile or Fishing rolls per day. Foragers can smoke meat and fish over a fire and add it to the regular store of rations. <br><br>The GM can impose penalties in areas with little plant or animal life (e.g., -3 in snow, -6 in desert), and cumulative penalties for repeated foraging in an area.
>
> >[!Planning DMScreen]- [[GURPS 4th - Wilderness Adventures.pdf#page=20|Planning]]
>A trip goes best when planned, though this isn’t always up to the travelers. Planning tasks come first for the heroes – but for the GM to handle these, he must skip forward to Covering Ground ([[GURPS 4th - Wilderness Adventures.pdf#page=23|p.23]]) and calculate how many days each leg of the journey will take, given the group’s means of locomotion. <h3>Knowing What You’re Getting Into</h3> A suitable Area Knowledge roll will reveal a region’s terrain type(s), and then a Survival roll for each terrain type will elaborate on current travel conditions and common dangers in such territory (the GM may require relevant Hidden Lore rolls to know uncommon dangers). In town, one PC with access to books and maps can take a week to try a Research roll to cover all such tasks for the entire trip. Whatever skills are used, failure discovers nothing and critical failure gives dangerously flawed details . . . thus, a sloppy researcher can doom an entire expedition. If the delvers are explorers, Terra Incognita (above) applies and none of this matters! <h3>Planning a Route</h3> Adventurers with a series of clear checkpoints and several routes between them can decide which way to go at any juncture up to when they must choose. If they made appropriate Area Knowledge and Survival rolls, or a Research roll, in town, the GM should reveal terrain type and estimated travel time along each leg; apply Covering Ground ([[GURPS 4th - Wilderness Adventures.pdf#page=23|p.23]]) to the slowest party member, and simply ignore the randomness of Mitigating Circumstances ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]-[[GURPS 4th - Wilderness Adventures.pdf#page=23|23]]) and Nasty Weather ([[GURPS 4th - Wilderness Adventures.pdf#page=30|p.30]]-[[GURPS 4th - Wilderness Adventures.pdf#page=31|31]]). This lets them plot a course and lay in supplies, including terrain-specific gear. If the group’s path is chosen for them – as when guarding a caravan – the itinerary won’t be their decision, but they can still prepare for the environment. <h3>Winging It</h3> Heroes in the field can gauge the terrain in a known area ahead by using Area Knowledge, and then use Survival to estimate the time to travel a given distance over it, as above. It’s too late for Research or shopping, however. <h3>Really Winging It</h3> Explorers in Terra Incognita ([[GURPS 4th - Wilderness Adventures.pdf#page=20|p.20]]) – and travelers who lack the correct skills – never get advance rolls to know terrain or estimate travel time. They can try Scouting (pp. 25-26), however. If this succeeds, roll against Naturalist or any Survival specialty to determine what terrain type lies ahead, unless that’s obvious (like towering mountains). Alternatively, if the group has a clear goal – seeking or avoiding a particular terrain type, minimizing distance or travel time, etc. – someone with Intuition may use it to pick the best path for that purpose.
>
> >[!Actual Travel DMScreen]- Actual Travel
>Unless the adventurers can teleport, they and all their stuff will need to get from A to B – probably with a side-trip to C for some looting. This is another matter best planned before leaving, though hikers who steal horses and riders whose mounts (coincidentally) go missing might change modes mid-journey. <h3>Feet</h3> The most basic means of traveling is walking or some variation on it. For all options, start with Basic Move and adjust for encumbrance (p. B17) to find the Move used with Covering Ground ([[GURPS 4th - Wilderness Adventures.pdf#page=23|p.23]]). For everything except hiking, ignore Terrain Types ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]) in suitable conditions and instead modify Move as noted, keeping fractions. Each method involves its own skill; for effects, see Harder Than It Looks ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]). <ul><li>Hiking: One foot in front of the other. Move is unmodified. Affected normally by terrain. Uses Hiking.</li><li>Sandshoeing: Inspired by lizard men. Requires sand. Replace terrain effects (typically Move ¥0.20) with a flat Move ¥0.50. Uses Hiking.</li><li>Skating: Glide like a barbarian – on blades. Requires ice! Replace terrain effects with Move ¥1.25 on a level surface, Move ¥0.50 anywhere else. Uses Skating. (This skill isn’t on any standard template, but assume that where Hiking or Skiing appears, Skating is also an option.) </li><li>Skiing: Slide like a barbarian. Needs snow! Replace terrain effects with Move ¥1.00 in general, Move ¥0.50 on uphill treks. Uses Skiing. </li><li>Snowshoeing: Traipse like a grouse. Yes, more snow. Replace terrain effects with a flat Move ¥0.50 (a big improvement over ¥0.20). Uses Hiking.</li></ul> <h3>Beasts</h3> Heroes with money, large animal Allies, or druidic powers might have a beast do all the work. To find the Move used for Covering Ground ([[GURPS 4th - Wilderness Adventures.pdf#page=23|p.23]]), begin with the creature’s Basic Move; adjust for encumbrance (p. B17), including the weight of the rider, his gear, and riding equipment; and multiply for Enhanced Move, if any (¥1.5 at level 0.5, ¥2 at level 1, ¥4 at level 2, and so on). Unless the animal has Terrain Adaptation, Terrain Types ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]) applies normally. Use Riding skill with Harder Than It Looks ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]). <h3>Wheels</h3> Beasts can instead pull land vehicles (p. 19) that have Load and Top Speed stats. Total passenger and cargo weight can’t exceed Load, while Top Speed acts as Move for Covering Ground ([[GURPS 4th - Wilderness Adventures.pdf#page=23|p.23]]). Use Move ¥1.00 on a good road – or ¥0.50 on a lousy road or off-road on flat terrain such as plains – instead of using Terrain Types ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]). On worse ground, stack Move ¥0.50 and terrain effects; e.g., mountain (¥0.20) results in a net ¥0.10. The skill to use with Harder Than It Looks ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]) is Teamster; though this isn’t on any standard template, assume it’s an option wherever Animal Handling or Riding appears. <h3>Boats</h3> Boats are vehicles (p. 19) with Load and Top Speed stats. Passenger weight plus cargo weight can’t exceed Load, and treat Top Speed as Move for Covering Ground ([[GURPS 4th - Wilderness Adventures.pdf#page=23|p.23]]). Terrain doesn’t matter as such, but water is often ice in arctic terrain or absent in desert – and going up mountains in a boat isn’t usually an option! Use Boating skill with Harder Than It Looks (below). If the boat sails (or glides along on magic), it offers one huge advantage: travel can be 24 hours/day, as long as somebody stands watch. Such vessels use Seamanship instead.<h3>Cool Rides</h3> Fantasy heroes love fantasy transportation! There are endless possibilities, but some basic principles apply: <ul><li> Animals use Basic Move modified for encumbrance and Enhanced Move as in Beasts (above). Being muscle-powered limits daily travel time ([[GURPS 4th - Wilderness Adventures.pdf#page=23|p. 23]]), but most critters are faster and/or stronger than people.</li><li>Vehicles use their Top Speed stat as Move, and can carry up to their Load stat instead of worrying about encumbrance. Those powered by magic, sails, etc. rather than muscle can travel for 24 hours/day, unless something prevents this. Land transport is affected by Terrain Types ([[GURPS 4th - Wilderness Adventures.pdf#page=22|p.22]]), unless it boasts Terrain Adaptation, moves on blades or skids (terrain works as for skating or skiing; see Feet, above), or has wheels (terrain works as for Wheels, above). Water transport ignores Terrain Types but must follow water. </li><li> Aerial transport ignores Terrain Types and can go anywhere. Some generic examples: <ol><li>Flying Carpet: Has Top Speed and Load fixed by magic, ignores terrain, and can fly for 24 hours/day as long as someone with Magery is awake. A flying ship is similar, but anyone with Seamanship can stand watch.</li><li>Iceboat: A wind-powered land vehicle, with Top Speed and Load stats. Moves on ice as if skating. Requires athletic handling, limiting daily travel time to that for muscle-powered transportation. </li><li>Walking Hut: Has Top Speed and Load set by magic, experiences standard terrain effects, and can walk for 24 hours/day as long as someone with Magery is awake.</li><li>Winged Beast: An animal with air Move. Affected by encumbrance but not by terrain. Muscle-powered, which limits daily travel time. Anything flying, ultra-fast, or untiring makes travel less of an adventure. Such transportation should have a high cash or point cost, if available, and demand a rarely taught skill: Piloting (Contragravity), Driving (Hut), Riding (Gryphon), etc.</li></ol></li></ul>
>
> >[!Scouting DMScreen]- Scouting
>A party trying to reconnoiter as it travels has three options: <ol><li>Send fast movers ahead while moving. As Covering Ground (p. 23) notes, this limits scouting to those who are at least 50% faster than the bulk of the group, but it doesn’t slow progress. It also doesn’t limit stealth. </li><li> Stop periodically to send people ahead. This halves daily travel distance, but anyone who wants to scout may try, and may do so stealthily. Travelers who aren’t scouting can use up to half the daily travel time for other tasks. </li><li> Scout in force. The whole party reconnoiters while moving at full speed, but stealth is a casualty. (If everyone moves slowly enough to preserve stealth, that’s the previous case: stealthy scouting at half travel speed.) These approaches affect Scouting Ahead (Dungeons, p. 7) as described in the next two sections. </li></ol><h3>Sneaking</h3> To reconnoiter undetected, fast movers or people sent ahead must roll against Stealth. A party scouting in force can still try to be stealthy but uses the group’s lowest Stealth, at -5 for haste – and the largest SM among the adventurers and their mounts and vehicles modifies enemy Vision. Here and in all later rules, Stealth failure – blown skill rolls, Quick Contests lost to sentries, successful enemy Perception rolls against those not using Stealth, etc. – means being detected . . . if there are enemies around! There might not be. If there are, only the adventurers out reconnoitering are in danger. Usually. <ul><li><i>Where Did That Come From?</i> In all cases, anyone handling a mount or a vehicle uses the lower of Stealth or the applicable Boating, Riding, or Teamster skill. </li><li><i>Size Matters:</i> Against an active sentry, the Stealth attempt becomes a Quick Contest against Vision. Remember that SM modifies Vision! A pixie (SM -6) or someone who can shapeshift into a rat (SM -7) can sneak even with mediocre skill. Those not moving on foot had better be good – a horse has SM +1, a wagon has SM +2, and so on. </li><li><i>Stealth from Above:</i> Flying characters can’t sneak but can fly high enough to be hard to see. The flyer may pick a range penalty of any size (although the GM might set limits, even in fantasy). His enemies get a Vision roll at this modifier – cumulative with SM – to spot him flying search patterns. The spy’s own Vision, Observation, Tracking, Traps, etc. (see Information Gathering, below) suffer the same distance penalty. Both sides add Acute Vision, and ignore -2 per level of Telescopic Vision. Thus, this works best for, say, an SM -4 hawk or SM -6 pixie with excellent eyesight. </li><li><i>It’s Just a Mouse:</i> When the scout outwardly resembles a beast, the guidelines under Critters (pp. 12-14) hold. Being seen won’t provoke hostility unless either the observer has cause to be wary of animal scouts or the creature is remarkable for the surroundings and the viewer makes his Naturalist roll to realize this. </li></ul><h3>Information Gathering</h3> Spotting buildings, counting orcs, noticing smoke, and so on requires no special roll. Most other things do, including: <ul><li><i>The Hills Have Ears:</i> If the goal is to get close enough to hear speech without being noticed, then scouting in force, with mounts, or in vehicles won’t work. People ahead of the party on foot (and flyers who risk landing) may roll an additional Quick Contest of Stealth vs. enemy Hearing. Winning means getting close enough for a Hearing roll. Losing works like any Stealth failure. </li><li><i>Lay of the Land:</i> Gathering enough information to guess at upcoming terrain (Really Winging It, p. 21) calls for a Naturalist or Survival roll. Terrain is obvious once you’re in it, so a useful prediction calls for someone to use one of the first two scouting options. If he lacks suitable nature skills, he can use Observation to collect details for someone else – but failure gives his associate a penalty equal to the margin. Observation can act as a complementary skill to the daily Cartography rolls under Mapping (p. 27), too; if also surveying terrain, roll separately for each task. All this assumes the scout can somehow communicate with the naturalist or mapper; animals aren’t much good at this. </li><li><i>Look, Footprints!</i> Those scouting may also look for a trail. Picking this up initially is a Tracking roll at the penalty under Terrain Types (p. 22).</li><li><i>I See Trouble Up Ahead:</i> Detecting an ambush involves an Observation roll. Noticing a trap uses Per-based Traps. Either must win a Quick Contest against any enemy Camouflage skill in use – and most wilderness foes do take this precaution.</li></ul>
>
> >[!There and Back Again DMScreen]- There and Back Again
>Knowing where you’ve been is as important as looking ahead! <h3>Getting Lost</h3> The GM decides whether the adventurers can get lost on their current adventure. If they’re following a road or a person (Tracking, pp. 30-31), or heading toward a visible, static landmark (mountain, ray of celestial light stabbing down from the heavens, etc.), this shouldn’t happen. Explorers who have Absolute Direction don’t get lost, either – skip this rule for a party that includes even one such individual. But if the heroes are roaming through trackless arctic or desert terrain, thick jungle or woodlands, supernatural mists, etc., the GM may require daily rolls to remain on course. Use Navigation anywhere, Area Knowledge in known parts, Observation for flyers, or a spell such as Find Direction, Know Location, or Pathfinder. If none of that applies, use IQ at -5. Make one roll for the highest score in the group – or, if everyone is trusting a guide without second thoughts, use that person’s best applicable ability. Also do this after a tracking mission (Bounty Hunting, pp. 47-48), if the party’s quarry knew the territory better than they did. Failure means getting lost. The adventurers make no progress toward their goal. They can perform all usual wilderness tasks, but waste one day’s worth of supplies and travel, and face the joys of Camping (pp. 24-25), Natural Threats (pp. 30-35), and Wandering Monsters (p. 56) for another day. If it matters where the delvers strayed, the GM can roll for a random direction (see Maps, pp. 52-53) or send them somewhere interesting (Lost, p. 48); either way, limit deviations to half a day’s travel so that a day is “there and back again.” Each day after that, they may try one of the above rolls, an IQ roll for somebody with Eidetic Memory, Tracking (modified by Terrain Types, p. 22) to retrace their trail, or the Remember Path spell. Success resumes travel; failure costs another day. Someone with Photographic Memory can get the party on track after one day, no roll required. The Forest of No Return: There are cursed, unnatural regions that want visitors to get lost! Some magical fogs have this effect even in known parts. In those situations, all the skill and spell rolls above are at -5 to -10; people with Absolute Direction must roll to avoid getting lost, though they ignore -3 of the penalty; and travelers with Photographic Memory have to roll to get back on track, but avoid -5 of the penalty. <h3>Getting Separated</h3> Anywhere the party could get lost, individuals or small groups detached for Scouting (pp. 25-26), foraging (Food and Water, pp. 42-44), etc. – or fleeing combat or pursuit – may get separated from their allies. Such people must roll as for Getting Lost (above) to reach their rendezvous point (which might be overrun, if they fled combat!). Otherwise, they or their allies will have to use magic (like Seeker) or Signaling (p. 28) to find each other. The first attempt to regroup wastes no appreciable time, but later ones cost a day apiece. Days spent searching allow no travel, and each fragment of the group faces Wandering Monsters (p. 56) on its own.<h3>Mapping</h3> With a day’s travel often subsumed into a few rolls for weather, daily progress, and random badness, the “GM describes, players inscribe” model recommended in Mapping (Dungeons, p. 6) isn’t viable. Describing everything would grow tedious – and anyway, it’s the rare maniac who’d spend eight or more hours sketching the trail a yard at a time. It’s fairer and less annoying for everyone if the GM reveals progressively more of his map (Maps, pp. 52-53) to the players. <ul><li><i>Mapmaker, Mapmaker, Make Me a Map:</i> Player knowledge provides no guarantees for the explorers’ map! The GM should make a daily Cartography roll in secret for each mapper. Keep a running total as follows: critical success gives +1, success adds 0, failure is -1, and critical failure is -2. Each day’s roll is at a modifier equal to the current tally plus the effects of any complementary Observation roll (Information Gathering, p. 26). This total matters for the next two rules.</li><li><i>Terra Cognita:</i> Mapped areas are no longer subject to Terra Incognita (p. 20) for the purpose of later Travel Arrangements (pp. 20-21), and can be used for the Navigation rolls in Following Directions (pp. 22-23) and Getting Lost (p. 26). When the heroes use their map-in-progress this way, apply its current running total as a skill modifier. </li><li><i>Maps-R-Us:</i> The running total at journey’s end determines map quality. In the lingo of Sages, p. 14, any penalty indicates a sketchy map, the sort that might sell for $25; 0 means an average map that would go for $50; and a bonus corresponds to an annotated map that rates an extra $50 per +1. These are base prices. An original map of new territory should rack up at least twice as much; a private commission, at least 10 times base price, plus time and expenses. This rule replaces Selling the Tale (Dungeons, p. 15).</li></ul>
>
> >[!Tracking DMScreen]- [[GURPS 4th - Wilderness Adventures.pdf#page=27|Tracking]]
>Tracking (Dungeons, p. 5) works normally for wilderness adventures set on land – but if that’s the whole point of the story, it deserves some elaboration. <ul><li><i>Days on the Trail:</i> Instead of rolling vs. Tracking once for the whole adventure, check daily, using the more-detailed modifiers under Terrain Types (p. 22) and Nasty Weather (pp. 30-31). Any success lets the trackers follow the trail at full speed. Failure or critical failure wastes time, subtracting 10% or 20%, respectively, from travel speed. Use these rules instead of those for Following Directions (pp. 22-23), as the hunters don’t get to pick the route – that’s at their quarry’s discretion. Ignore Getting Lost (p. 26) for the same reason, though the heroes might have to roll at the end of the hunt to see whether they know where they’ve ended up! </li><li><i>Hot on the Trail:</i> If time is of the essence, the GM should set the initial lead that the heroes’ quarry enjoys. Then looking at their prey’s stats, use Travel (pp. 20-24) to establish a plausible daily travel distance for the target and add that to the lead each day. Work out the pursuers’ daily distance normally – remembering that time spent on tasks other than pursuit is time wasted – and subtract that from the lead each day. If the result is zero or negative, the adventurers overtake their target that day and successful Scouting (pp. 25-26) can spot him. </li><li><i>Losing the Trail:</i> To keep things interesting, these rules assume that critical failure at Tracking merely slows the trackers. If the GM prefers, critical failure might mean losing the trail completely. Instead of a 20% speed penalty, the party makes no progress that day while their quarry widens his lead. The party can try a Tracking roll each day, with success meaning normal progress again but any failure wasting another day.</li><li><i>Active Countermeasures:</i> Someone who knows he might be tracked can try to thwart this. Success at the Light Walk skill (a secret of martial artists, ninja, and elves) makes tracking impossible without a sense other than sight; e.g., Discriminatory Smell. The Hide Path spell inflicts a flat -8 on the trackers’ roll, while Walk Through Plants gives -1d if there are any plants at all, with an extra -2 in jungle or woodlands. Taking mundane precautions allows a traveler to turn Tracking attempts against him into Quick Contests vs. his own Tracking by reducing his daily speed by 10% (the False Tracks spell lets him use Naturalist at no speed penalty) – and if the trackers lose, they suffer an effective critical failure.</li></ul>

---

>[!Recovery]- Recovery
> >[!Recovering From Unconsciousness DMScreen]- Recovering from Unconsciousness
>Failure by 5 or more on a knockdown roll, a failed HT roll to stay conscious at 0 HP or less, and many other things (e.g., certain critical hits) can leave you unconscious. <br>
>It is up to the GM to decide whether you are truly unconscious or just totally incapacitated by pain and injury – but either way, you can’t do anything. <br><br>You recover as follows: <br> - If you have 1 or more HP remaining, you awaken automatically in 15 minutes.  At 0 HP or worse, but above -1\*HP, make a HT roll to awaken every hour. Once you succeed, you can act normally. You do not have to roll against HT every second to remain conscious unless you receive new injury. But since you are below 1/3 your HP, you are at half Move and Dodge. <br> - At -1\*HP or below, you are in bad shape. You get a single HT roll to awaken after 12 hours. If you succeed, you regain consciousness and can act as described above. But if you fail, you won’t regain consciousness without medical treatment – use the rules given under Stabilizing a Mortal Wound (p. 424). Until you receive help, you must roll vs. HT every 12 hours; if you fail, you die. <br> - If you have 1 or more HP remaining, you awaken automatically in 15 minutes. 
>
> >[!Natural Recovery DMScreen]- Natural Recovery
>Rest lets you recover lost HP, unless the damage is of a type that specifically does not heal naturally (for an example, see Illness, p. 442). At the end of each day of rest and decent food, make a HT roll. On a success, you recover 1 HP. The GM may give a penalty if conditions are bad, or a bonus if conditions are very good.
>
> >[!First Aid DMScreen]- First Aid
>The two main uses for First Aid skill (p. 195) are bandaging and treating shock. <h3>Bandaging</h3> It takes one minute to apply pressure or a tourniquet to stop bleeding. This restores 1 HP. <br>Using the Bleeding rule (p. 420), someone who is wounded but receives a successful First Aid roll within one minute of his injury loses no HP to bleeding. A later roll will prevent further HP loss. <h3>Treating Shock</h3> After bandaging, the aid-giver may take extra time to apply a more elaborate dressing and treat the victim for shock. He must keep the victim warm, comfortable, calm, and still. After the time indicated on the First Aid Table, he may roll against First Aid skill. <br>On a success, the medic rolls as indicated on the table to see how many HP the victim recovers – minimum 1 HP. A critical success restores the maximum possible HP! This roll includes the 1 HP for bandaging; thus, a roll of 1 HP restores no further HP. On a critical failure, the victim loses 2 HP instead of recovering any HP at all! 
> > >[!First Aid Table DMScreen]- First Aid Table
| Tech Level | Time per Victim | HP Restored |
| ---------- | --------------- | ----------- |
| 0-1        | 30 minutes      | 1d-4        |
| 2-3        | 30 minutes      | 1d-3        |
| 4          | 30 minutes      | 1d-2        |
| 5          | 20 minutes      | 1d-2        |
| 6-7        | 20 minutes      | 1d-1        |
| 8          | 10 minutes      | 1d          |
| 9+         | 10 minutes      | 1d+1        |
>
> >[!Surgery DMScreen]- Surgery
>Surgery can physically repair damage to the body, but it’s risky at low TLs – especially prior to the invention of anesthesia (mid-TL5) and blood typing (TL6). See Surgery skill (p. 223) for general modifiers and for the effects of a failed skill roll. <br><br>Some additional rules: <br> - Equipment: Basic equipment gives -6 at TL1, -5 at TL2-3, -4 at TL4, -2 at TL5, and +(TL-6) at TL6+. Equipment quality further modifies the roll; see Equipment Modifiers (p. 345). The modifiers for TL5+ surgery assume that anesthetic is available. If it isn’t, apply a -2 penalty to skill. This is instead of the usual -1 for a missing item. <br><br> - Infection: Before TL5 (and, at the GM’s option, even during much of TL5), antiseptic practice is poor. Check for infection (see Infection, p. 444) after any surgery. <h3>Stabilizing a Mortal Wound</h3> Each attempt takes one hour. The roll is at -2 if the patient is at -3\*HP or worse, or -4 if he’s at -4\*HP or worse. On a failure, repeated attempts are allowed, at a cumulative -2 per attempt. If the victim dies on the table, resuscitation may be possible; see Resuscitation (p. 425). <h3>Repairing Lasting Crippling Injuries</h3> It is possible to fix a lasting crippling injury (see Duration of Crippling Injuries, p. 422) through surgery rather than leaving it to heal on its own. This takes 2 hours. On a success, measure the injury’s remaining recovery time in weeks rather than months. But on a critical failure, the injury becomes permanent! <h3>Repairing Permanent Crippling Injuries</h3> Radical surgery can fix certain permanent crippling injuries at TL7+; exact details are up to the GM. This often requires prosthetic or transplant parts, which might be costly or hard to find. At TL7-8, the procedure might only restore partial functionality. This kind of operation is also tricky: -3 or worse to skill. On a failure, the patient needs 1d months to recover before another attempt is possible.
>
> >[!Medical Care DMScreen]- Medical Care
>Anyone under the care of a competent physician (Physician skill 12+) gets +1 on all rolls for natural recovery. <br><br>The *healer* may also make a Physician roll to cure the patient. Only one physician may roll per patient, but a single physician can care for up to 200 patients. The exact number of patients a physician can attend to and the frequency with which he may roll to cure them depend on the TL of his Physician skill; see the Medical Help Table, below. On a success, the patient recovers 1 HP; on a critical success, he recovers 2 HP. This is in addition to natural healing. However, a critical failure costs the patient 1 HP!<br><br>High-tech physicians depend heavily on equipment but still receive good basic training; therefore, a TL6+ physician performs as though he were TL6 if he has to make do without the gadgetry to which he is accustomed, as long as the surroundings are clean.
> > >[!Medical Help Table DMScreen]- Medical Help Table
|Tech Level|Frequency of Rolls|Patients per Doctor|
|---|---|---|
|0|No physicians. Self-care only.|-|
|1-3|Weekly|10|
|4|Every 3 days|10|
|5|Every 2 days|15|
|6|Daily|20|
|7|Daily|25|
|8|Daily|50|
|9|2× daily|50|
|10|3× daily|50|
|11|4× daily|100|
|12+|5× daily|200|
>
> >[!Resuscitation DMScreen]- Resuscitation
>Reviving a drowning, asphyxiation, or heart attack victim requires resuscitation. Make a successful Physician/TL7+ roll – or a First Aid/TL7+ roll at -4. Each attempt takes one minute. Repeated attempts are possible, but there is almost always a time limit. <br><br>Cardiopulmonary resuscitation (CPR) and rescue breathing, widely taught after 1960, are more effective than earlier forms of resuscitation. First Aid rolls (but not default rolls) to revive victims of drowning or asphyxiation are at -2 instead of -4.

---

>[!Fatigue DMScreen]- Fatigue
> >[!Lost Fatigue Points DMScreen]- Lost Fatigue Points
>The chart below summarizes the effects of being at low or negative FP. All effects are cumulative. <br><br>- Less than 1/3 your FP left – You are very tired. Halve your Move, Dodge, and ST (round up). This does not affect ST-based quantities, such as HP and damage.<br><br>- 0 FP or less – You are on the verge of collapse. If you suffer further fatigue, each FP you lose also causes 1 HP of injury. Thus, fatigue from starvation, dehydration, etc. will eventually kill you – and you can work yourself to death! To do anything besides talk or rest, you must make a Will roll; in combat, roll before each maneuver other than Do Nothing. On a success, you can act normally. You can use FP to cast spells, etc., and if you are drowning, you can continue to struggle, but you suffer the usual 1 HP per FP lost. On a failure, you collapse, incapacitated, and can do nothing until you recover to positive FP. On a critical failure, make an immediate HT roll. If you fail, you suffer a heart attack; see Mortal Conditions (p. 429).<br><br>- -1¥FP – You fall unconscious. While unconscious, you recover lost FP at the same rate as for normal rest. You awaken when you reach positive FP. Your FP can never fall below this level. After this stage, any FP cost comes off your HP instead!
>
> >[!Recovering From Fatigue DMScreen]- Recovering From Fatigue
>You can recover “ordinary” lost FP by resting quietly. Reading, talking, and thinking are all right; walking around, or anything more strenuous, is not. Lost FP return at the rate of 1 FP per 10 minutes of rest. The GM may allow you to regain one extra FP if you eat a decent meal while resting. Certain drugs, magic potions, etc. can restore missing FP, as can spells such as Lend Energy and Recover Energy (see p. 248). <br><br>You can only recover from fatigue caused by missed sleep by sleeping for at least one full sleep period. This restores 1 FP. Further uninterrupted sleep restores 1 FP per hour. <br><br>You need food or water to recover FP lost to starvation or dehydration; see Starvation and Dehydration (above).
>
> >[!Fatigue Costs DMScreen]- Fatigue Costs
>The following activities commonly result in FP loss. <h3>Fighting a Battle</h3> Any battle that lasts more than 10 seconds will cost FP – you expend energy quickly when you fight for your life! Those who make no attack or defense rolls during the fight are exempt from this fatigue, but other actions (e.g., casting magic spells) still have their usual FP cost. Assess the following costs at the end of the battle: No Encumbrance: 1 FP. Light Encumbrance: 2 FP. Medium Encumbrance: 3 FP. Heavy Encumbrance: 4 FP. Extra-Heavy Encumbrance: 5 FP. If the day is hot, add 1 FP to the above – or 2 FP for anyone in plate armor, an overcoat, etc. Full-coverage armor at TL9+ is climate-controlled. This counts as a cooling system, and negates the penalties for hot weather. These costs are per battle, not per 10 seconds of battle. A very long battle may cost more (GM’s decision), but it would have to run for 2 or 3 minutes (120 to 180 turns!) before extra FP costs would be realistic. <h3>Hiking</h3>Use the FP costs for fighting a battle, but assess them per hour of road travel; e.g., one hour of marching with light encumbrance costs 2 FP (3 FP on a hot day). If the party enters combat while on the march, assume they’ve been walking for an hour, unless events dictate otherwise, and assess fatigue accordingly. <h3>Overexertion</h3>Carrying more than extra-heavy encumbrance, or pushing/pulling a very heavy load, costs 1 FP per second (see Lifting and Moving Things, p. 353). For FP costs for other forms of heavy exertion, see Extra Effort (p. 356). <h3>Running or Swimming</h3> Every 15 seconds of sprinting, or minute of paced running or swimming, requires a HT roll to avoid losing 1 FP. Encumbrance has no direct effect on this, but you run or swim more slowly. See Running (p. 354) and Swimming (p. 354). <h3>Special Abilities</h3> Most magic spells (see Chapter 5), many advantages (such as Healing, p. 59), and a few cinematic skills (for instance, Power Blow, p. 215) cost FP to use, as does any trait with the Costs Fatigue limitation (p. 111).
>
> >[!Starvation and Dehydration DMScreen]- Starvation and Dehydration
>When you buy equipment, don’t forget food! The traveler’s rations under Camping and Survival Gear (p. 288) are the minimum necessary to keep you healthy on the road; missing even one meal weakens you. *Note to the GM: If keeping up with the party’s meals doesn’t sound like fun, feel free to ignore this whole section. Travel is much more hazardous if you have to keep track of food and water!* <h3>Starvation</h3>A human needs three meals per day. For each meal you miss, take 1 FP. You can only recover “starvation” fatigue with a day of rest: no fighting or travel, and three full meals. Each day of rest makes up for three skipped meals.<h3>Dehydration</h3>In temperate areas, where water is easy to come by, assume that you can renew your supplies as needed. But if water is in short supply, watch out! A human (or elf, dwarf, etc.) needs 2 quarts of water a day – 3 in hot climates, 5 in the heat of the desert! If you get less than you need, you lose 1 FP every eight hours. If you drink less than a quart a day, you lose an extra 1 FP and 1 HP per day. You can regain all FP lost to dehydration after a day of rest with ample water supplies. You recover lost HP at the usual rate.
>
> >[!Missed Sleep DMScreen]- Missed Sleep
>The average human can function for a 16-hour “day.” He must then rest for an eight-hour “sleep period.” Less Sleep (p. 65) shortens this sleep period, thereby increasing useful day length; Extra Sleep (p. 136) and Sleepy (p. 154) do the opposite. Getting less sleep than your sleep period costs FP that you can only recover by sleeping. <br><br>Interruptions, noise, and disadvantages such as Chronic Pain (p. 126), Insomniac (p. 140), Light Sleeper (p. 142), and Nightmares (p. 144) can reduce the quality of your sleep. In game terms, your sleep counts as fewer hours – or none at all. <br><br>Those who have the Doesn’t Sleep advantage (p. 50) can ignore this entire section!
>
> >[!Staying Up Late DMScreen]- Staying Up Late
>If you’ve been awake for more than your normal day (typically 16 hours), you start to get tired. You lose 1 FP if you fail to go to sleep, and 1 FP per quarter-day (usually four hours) you stay awake after that. <br><br>If you’ve lost half or more of your FP to lack of sleep, you must make a Will roll every two hours you spend inactive (e.g., standing watch). On a failure, you fall asleep, sleeping until you are awakened or get a full night’s sleep. On a success, you have -2 to DX, IQ, and self-control rolls. Those with the Slow Riser disadvantage (p. 155) get an extra -1. <br><br>If you’re down to less than 1/3 your FP due to lack of sleep, roll as above once per 30 minutes of inaction or two hours of action. This can be very dangerous!
>
> >[!Getting Up Early DMScreen]- Getting Up Early
>If you sleep for less than your full sleep period, you’ll still be tired when you wake up. Subtract twice the hours of missed sleep from your day to determine how long you can stay awake. For example, if your sleep period is eight hours and you sleep only six hours, you’ve missed two hours of sleep. You will suffer the effects of staying up late after only 12 hours: your usual 16-hour day, minus four hours (twice your hours of missed sleep).
>

---

>[!Created Spells]- Created Spells
><h3>Powers as Magic</h3>
>
>```dataview 
>TABLE WITHOUT ID file.link AS "Spell", impulse as "Impulse", aspect as "Aspect",  spellCost as "Cost" FROM "TTRPG Systems" WHERE contains(tags, "PowersAsMagic") SORT Cost ASC 
>```

---

>[!DMTools DMScreen]- DM Tools
>[[Roll Calculator|Roll Calculator]]

---

>[!PowersAsMagic DMScreen]- Powers as Magic
> > [!SpellList DMScreen]- Spells
> > >```dataview 
TABLE WITHOUT ID  file.link AS "Spells", spellCost as "Vraul Cost", castTime as "Cast Time", impulse as "Impulse", aspect as "Aspect" FROM "Library"  WHERE contains(tags, "PowersAsMagic") and contains(tags, "Spell") SORT spellCost ASC
> > >```
>
> >[!Aspects DMScreen]- Aspects
 > > >```dataview 
TABLE WITHOUT ID 
file.link AS "Aspect", manaCost as "Vraul Cost", characterPointCost as "Character Points Required", requiredRealm as "Required Realm" FROM "Library"  WHERE contains(tags, "PowersAsMagic") and contains(tags, "Nouns") SORT spellCost ASC
> > >```
>
> >[!Impulses DMScreen]- Impulses
 > > >```dataview 
TABLE WITHOUT ID file.link AS "Impulse", fpCost as "FP Cost", castTime as "Cast Time" FROM "Library"  WHERE contains(tags, "PowersAsMagic") and contains(tags, "Verbs") SORT spellCost ASC
> > >```

---
