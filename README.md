# news-rss
a quick and dirty way to pull RSS feeds and launder their original sources

some RSS readers won't allow you to use Google News as a source for your RSS feeds (or at least they won't let you do that without a paid subscription)

some news sites don't offer by-topic RSS feeds

some RSS feed creators have gotten crappy

thus this repo, which will pull use Google News RSS xml as a base for the news outlets and topics you're interested in and re-publish them as xml files on Github.  you can then subscribe to the xml feed here, avoiding the association with Google News

## what to do
add an entry to feeds.json for any new sources you'd like to follow (make sure your json syntax is correct)

the code will make xml files for each entry in the json, output them to the /feeds folder, and also generate a copy-pasteable list of links to said feeds. just enter those links into your RSS reader
