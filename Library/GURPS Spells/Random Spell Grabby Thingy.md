
~~~datacorejsx

const { useState } = dc

return function View(){
    const spells = dc.useQuery(`@page and #SpellsAsMagic and path("Library")`);

    // Set minimums and maximums
    let min = 0
    let max = spells.length
    
    // Set random number
    const [randNum, setRandNum] = useState(Math.floor(Math.random() * (max - min) ) + min);

    function handleRefresh() { setRandNum(Math.floor(Math.random() * (max - min) ) + min);
    }

    let filePath = spells[randNum].$path;
    let useFile = dc.useFile(filePath);
    
    return (
    <div>
        <dc.Markdown content={`~~~statblock
layout: GCS - Layout 
name: [[${useFile.field("spellLink").raw}|${useFile.field("spellName").raw}]]
spell_class: ${useFile.field("spellClass").raw}
resistedW: ${useFile.field("spellResisted").raw}
difficulty: ${useFile.field("spellDifficulty").raw}
duration: ${useFile.field("spellDuration").raw}
casting_cost: ${useFile.field("spellCost").raw}
maintenance_cost: ${useFile.field("spellMaintenance").raw}
casting_time: '${useFile.field("spellCastingTime").raw}'
college: ${useFile.field("spellCollege").raw}
prerequisites: ${useFile.field("spellPrereqText").raw}
reference: ${useFile.field("spellReference").raw}
spellLink: ${useFile.field("spellLink").raw}
spellTags: ${useFile.field("spellTags").raw}
source: ${useFile.field("spellSource").raw}
~~~`}/>
        <dc.Button onClick={handleRefresh}>Button</dc.Button>
    </div>
);
}
~~~


