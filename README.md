# Knowledge is graphs

The purpose of this repository is to collect sample [queries](https://query.wikidata.org/) for discovering HDF-related information in the [Wikidata knowledge graph](https://en.wikipedia.org/wiki/Wikidata).

## Relevant entities

- [Hierarchical Data Format (Q1069215)](https://www.wikidata.org/wiki/Q1069215)
- [HDF5 (Q61080677)](https://www.wikidata.org/wiki/Q61080677)
- [HDF4 (Q63065200)](https://www.wikidata.org/wiki/Q63065200)
- [Highly Scalable Data Service (Q114859023)](https://www.wikidata.org/wiki/Q114859023)
- [HDFView (Q130060108)](https://www.wikidata.org/wiki/Q130060108)

## Relevant properties

- [readable file format (P1072)](https://www.wikidata.org/wiki/Property:P1072)
- [writable file format (P1073)](https://www.wikidata.org/wiki/Property:P1073)

## Example

List subjects that are capable of reading or writing [HDF](https://www.wikidata.org/wiki/Q1069215):

```sparql
SELECT DISTINCT ?x ?xLabel ?url WHERE {
  { ?x wdt:P1072 wd:Q1069215 . }       # Something that can read HDF
  UNION
  { ?x wdt:P1073 wd:Q1069215 . }       # Something that can write HDF
  
  OPTIONAL { ?x wdt:P856 ?url. }       # Official website

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
[Try it!](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Fx%20%3FxLabel%20%3Furl%20WHERE%20%7B%0A%20%20%7B%20%3Fx%20wdt%3AP1072%20wd%3AQ1069215%20.%20%7D%20%20%20%20%20%20%20%23%20Something%20that%20can%20read%20HDF%0A%20%20UNION%0A%20%20%7B%20%3Fx%20wdt%3AP1073%20wd%3AQ1069215%20.%20%7D%20%20%20%20%20%20%20%23%20Something%20that%20can%20write%20HDF%0A%20%20%0A%20%20OPTIONAL%20%7B%20%3Fx%20wdt%3AP856%20%3Furl.%20%7D%20%20%20%20%20%20%20%23%20Official%20website%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D)
