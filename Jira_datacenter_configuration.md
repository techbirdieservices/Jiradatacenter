1. TO increase jiradatacenter indexing performace.
- Add below lines to jira-config.properties
jira.index.background.batch.size = 83200
jira.index.issue.maxqueuesize = 83200
jira.index.sharedentity.maxqueuesize = 83200

2. when jira indexsanpshot is not getting created due to snapshot size is more than 8GB.
- Add below lines to jira-config.properties
index.use.snappy = false
jira.index.snapshot.copy.archiver = zip

3. when upgradeing to 9.x to start auto-indexing. 
- #upgrade.reindex.allowed=false