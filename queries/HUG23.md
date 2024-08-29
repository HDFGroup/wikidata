# HUG23

List the presentation titles from the [HUG23](https://www.wikidata.org/wiki/Q126992704) event:

```sparql
SELECT DISTINCT ?talk ?talkLabel WHERE {
  wd:Q126992704 wdt:P527 ?talk .       # Something that is part of HUG23
 
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
```
[Try it!](https://query.wikidata.org/#SELECT%20DISTINCT%20%3Ftalk%20%3FtalkLabel%20WHERE%20%7B%0A%20%20wd%3AQ126992704%20wdt%3AP527%20%3Ftalk%20.%20%20%20%20%20%20%20%23%20Something%20that%20is%20part%20of%20HUG23%0A%20%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D)
