
### jira-config.properties

## To increase jiradatacenter indexing performace
- Add below lines to jira-config.properties
```sh
jira.index.background.batch.size = 83200
jira.index.issue.maxqueuesize = 83200
jira.index.sharedentity.maxqueuesize = 83200
```
## when jira indexsanpshot is not getting created due to snapshot size is more than 8GB.
- Add below lines to jira-config.properties
```sh
index.use.snappy = false
jira.index.snapshot.copy.archiver = zip
```

## when upgradeing to 9.x to start auto-indexing.
```sh
#upgrade.reindex.allowed=false
```
##
