
### Complete Spell List

```datacorejsx


const { useState } = dc;
    
return function View() {

    const [collegeFilter, setCollegeFilter] = useState('');
    const [typeFilter, setTypeFilter] = useState('');
    const [costFilter, setCostFilter] = useState('');
    const [nameFilter, setNameFilter] = useState('');
    const [prereqFilter, setPrereqFilter] = useState('');
    const [bookFilter, setBookFilter] = useState('');
    const [spells, setSpells] = useState(dc.useQuery(`@page and #SpellsAsMagic and path("Library")`));
    
    // console.log("This is spells:", spells)
    function prereqLinker(value, index, array) {

        if (spells.find((element) => element.$name == value)) {
            return "[[" + value + "]]"
        }
        else {
            return value
        }
    }

    // Refresh table
    function handleRefresh() {
    
    }

    const COLUMNS = [    
    { id: "Name", value: page => page.$link, pagination: true,},    
    { id: "Area", value: page => page.value("spellClass"),},    
    { id: "Cost", value: page => page.value("spellCost") },
    { id: "College", value: page => page.value("spellCollege") },
    { id: "Book", value: page => page.value("spellSource") },
    { id: "Prerequisites", value: page => page.value("spellPrerequisites").map(prereqLinker) }
];

    // Selecting `#game` pages, for example.    
    const pages = dc.useQuery(`@page and #SpellsAsMagic and path("Library") and spellName.contains("${nameFilter}") and spellClass.contains("${typeFilter}") and spellCost.contains("${costFilter}") and spellCollege.contains("${collegeFilter}") and spellPrerequisites.contains("${prereqFilter}") and spellCollege.contains("${bookFilter}")`);    
    
    // Uses the built in table component for showing objects in a table!    
    return (
    <div>
        <dc.Textbox placeholder="Name Filter" onChange={(e) => setNameFilter(e.target.value)}/>
        <dc.Textbox placeholder="Type Filter" onChange={(e) => setTypeFilter(e.target.value)}/>
        <dc.Textbox placeholder="Cost Filter" onChange={(e) => setCostFilter(e.target.value)}/>
        <dc.Textbox placeholder="College Filter" onChange={(e) => setCollegeFilter(e.target.value)}/>
        <dc.Textbox placeholder="Prerequisites Filter" onChange={(e) => setPrereqFilter(e.target.value)}/>
        <dc.Textbox placeholder="Books Filter" onChange={(e) => setBookFilter(e.target.value)}/>
        <dc.Button onClick={handleRefresh}>Refresh</dc.Button>
        <dc.Table columns={COLUMNS} rows={pages} paging={15}/>
        
    </div>
    );
}
```
^spellListSearch

---

