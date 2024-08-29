# Knowledge is graphs

The purpose of this repository is to collect sample [queries](https://query.wikidata.org/) for discovering HDF-related information in the [Wikidata knowledge graph](https://en.wikipedia.org/wiki/Wikidata).

## Relevant entities

- [Hierarchical Data Format (Q1069215)](https://www.wikidata.org/wiki/Q1069215)

## Relevant properties

- [readable file format (P1072)](https://www.wikidata.org/wiki/Property:P1072)
- [writable file format (P1073)](https://www.wikidata.org/wiki/Property:P1073)

## Example

```sparql
SELECT DISTINCT ?app ?appLabel WHERE {
  ?app wdt:P1072 wd:Q1069215 ;         # Something that can read HDF
        wdt:P1073 wd:Q1069215 .        # Something that can write HDF

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
[Try it!](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fapp%20%3FappLabel%20WHERE%20%7B%0A%20%20%3Fapp%20wdt%3AP1072%20wd%3AQ1069215%20%3B%20%20%20%20%20%20%20%20%20%23%20Somthing%20that%20can%20read%20HDF%0A%20%20%20%20%20%20%20%20wdt%3AP1073%20wd%3AQ1069215%20.%20%20%20%20%20%20%20%20%23%20Something%20that%20can%20write%20HDF%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D)
