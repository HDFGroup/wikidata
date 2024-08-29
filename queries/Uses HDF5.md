# Uses HDF5

```sparql
SELECT DISTINCT ?sth ?sthLabel WHERE {
  { ?sth wdt:P2283 wd:Q61080677. }      # Something that uses HDF5
  UNION
  { ?sth wdt:P4510 wd:Q61080677. }      # Something that describes a project that uses HDF5
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
[Try it!](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fsth%20%3FsthLabel%20WHERE%20%7B%0A%20%20%7B%20%3Fsth%20wdt%3AP2283%20wd%3AQ61080677.%20%7D%20%20%20%20%20%20%23%20Something%20that%20uses%20HDF5%0A%20%20UNION%0A%20%20%7B%20%3Fsth%20wdt%3AP4510%20wd%3AQ61080677.%20%7D%20%20%20%20%20%20%23%20Something%20that%20describes%20a%20project%20that%20uses%20HDF5%0A%20%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D)
