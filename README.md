# Configure Spark in Docker Components +

- Let's configure docker components in a local-like environment
- [spark:3.5.1-scala2.12-java17-python3-ubuntu](https://hub.docker.com/layers/library/spark/3.5.1-scala2.12-java17-python3-ubuntu/images/sha256-17f945959bb62af8e083ff2885095fb8f7f34e8fd7c10ef1bef7bed79a9c2bcb?context=explore)
 ```bash
$ $SPARK_HOME/bin/spark-shell --version
24/11/13 11:07:57 WARN Utils: Your hostname, LAPTOP-RALEOMTL resolves to a loopback address: 127.0.1.1; using 10.255.255.254 instead (on interface lo)
24/11/13 11:07:57 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.1
      /_/
                        
Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.13
Branch HEAD
Compiled by user heartsavior on 2024-02-15T11:24:58Z
Revision fd86f85e181fc2dc0f50a096855acf83a6cc5d9c
Url https://github.com/apache/spark
Type --help for more information.
```

## Try
```
$ docker compose up -d

# sudo apt install wslu
$ wslview http://localhost:8080
$ wslview http://localhost:8081
```

## URLs
- 

## Metrics
- https://dzlab.github.io/bigdata/2020/07/03/spark3-monitoring-1/
- https://dzlab.github.io/bigdata/2020/07/03/spark3-monitoring-2/
- https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-spark/
```
# Master
$ curl http://localhost:8080/metrics/master/prometheus/
$ curl http://localhost:8080/metrics/master/json/
$ curl http://localhost:8080/metrics/applications/prometheus/
$ curl http://localhost:8080/metrics/applications/json/

# Worker
$ http://localhost:8081/metrics/prometheus/
$ http://localhost:8081/metrics/json/

# Driver
$ http://localhost:4040/metrics/prometheus/
$ http://localhost:4040/metrics/executors/prometheus/

$ http://localhost:4040/streaming/

```
<details>
      <summary>Metrics ...</summary>
      
```
$ curl -s http://localhost:4040/api/v1/applications/app-20241114052829-0000 | jq
{
  "id": "app-20241114052829-0000",
  "name": "PythonStreamingNetworkWordCount",
  "attempts": [
    {
      "startTime": "2024-11-14T05:28:28.289GMT",
      "endTime": "1969-12-31T23:59:59.999GMT",
      "lastUpdated": "2024-11-14T05:28:28.289GMT",
      "duration": 885258,
      "sparkUser": "spark",
      "completed": false,
      "appSparkVersion": "3.5.1",
      "startTimeEpoch": 1731562108289,
      "endTimeEpoch": -1,
      "lastUpdatedEpoch": 1731562108289
    }
  ]
}

curl -s http://localhost:4040/api/v1/applications/app-20241114052829-0000/executors  | jq
[
  {
    "id": "driver",
    "hostPort": "9465cff6c180:39413",
    "isActive": true,
    "rddBlocks": 0,
    "memoryUsed": 148905,
    "diskUsed": 0,
    "totalCores": 0,
    "maxTasks": 0,
    "activeTasks": 0,
    "failedTasks": 0,
    "completedTasks": 0,
    "totalTasks": 0,
    "totalDuration": 1403261,
    "totalGCTime": 3839,
    "totalInputBytes": 0,
    "totalShuffleRead": 0,
    "totalShuffleWrite": 0,
    "isBlacklisted": false,
    "maxMemory": 455501414,
    "addTime": "2024-11-14T05:28:29.256GMT",
    "executorLogs": {},
    "memoryMetrics": {
      "usedOnHeapStorageMemory": 148905,
      "usedOffHeapStorageMemory": 0,
      "totalOnHeapStorageMemory": 455501414,
      "totalOffHeapStorageMemory": 0
    },
    "blacklistedInStages": [],
    "peakMemoryMetrics": {
      "JVMHeapMemory": 357990256,
      "JVMOffHeapMemory": 131278680,
      "OnHeapExecutionMemory": 0,
      "OffHeapExecutionMemory": 0,
      "OnHeapStorageMemory": 595325,
      "OffHeapStorageMemory": 0,
      "OnHeapUnifiedMemory": 595325,
      "OffHeapUnifiedMemory": 0,
      "DirectPoolMemory": 17369480,
      "MappedPoolMemory": 0,
      "ProcessTreeJVMVMemory": 0,
      "ProcessTreeJVMRSSMemory": 0,
      "ProcessTreePythonVMemory": 0,
      "ProcessTreePythonRSSMemory": 0,
      "ProcessTreeOtherVMemory": 0,
      "ProcessTreeOtherRSSMemory": 0,
      "MinorGCCount": 764,
      "MinorGCTime": 3839,
      "MajorGCCount": 0,
      "MajorGCTime": 0,
      "TotalGCTime": 3839
    },
    "attributes": {},
    "resources": {},
    "resourceProfileId": 0,
    "isExcluded": false,
    "excludedInStages": []
  },
  {
    "id": "0",
    "hostPort": "172.22.0.4:40571",
    "isActive": true,
    "rddBlocks": 0,
    "memoryUsed": 148905,
    "diskUsed": 0,
    "totalCores": 2,
    "maxTasks": 2,
    "activeTasks": 1,
    "failedTasks": 0,
    "completedTasks": 2866,
    "totalTasks": 2867,
    "totalDuration": 328974,
    "totalGCTime": 593,
    "totalInputBytes": 0,
    "totalShuffleRead": 605220,
    "totalShuffleWrite": 1168594,
    "isBlacklisted": false,
    "maxMemory": 94371840,
    "addTime": "2024-11-14T05:28:31.364GMT",
    "executorLogs": {
      "stdout": "http://172.22.0.4:8081/logPage/?appId=app-20241114052829-0000&executorId=0&logType=stdout",
      "stderr": "http://172.22.0.4:8081/logPage/?appId=app-20241114052829-0000&executorId=0&logType=stderr"
    },
    "memoryMetrics": {
      "usedOnHeapStorageMemory": 148905,
      "usedOffHeapStorageMemory": 0,
      "totalOnHeapStorageMemory": 94371840,
      "totalOffHeapStorageMemory": 0
    },
    "blacklistedInStages": [],
    "peakMemoryMetrics": {
      "JVMHeapMemory": 128602368,
      "JVMOffHeapMemory": 86829568,
      "OnHeapExecutionMemory": 0,
      "OffHeapExecutionMemory": 0,
      "OnHeapStorageMemory": 10090514,
      "OffHeapStorageMemory": 0,
      "OnHeapUnifiedMemory": 10090514,
      "OffHeapUnifiedMemory": 0,
      "DirectPoolMemory": 16932119,
      "MappedPoolMemory": 0,
      "ProcessTreeJVMVMemory": 0,
      "ProcessTreeJVMRSSMemory": 0,
      "ProcessTreePythonVMemory": 0,
      "ProcessTreePythonRSSMemory": 0,
      "ProcessTreeOtherVMemory": 0,
      "ProcessTreeOtherRSSMemory": 0,
      "MinorGCCount": 207,
      "MinorGCTime": 650,
      "MajorGCCount": 0,
      "MajorGCTime": 0,
      "TotalGCTime": 650
    },
    "attributes": {},
    "resources": {},
    "resourceProfileId": 0,
    "isExcluded": false,
    "excludedInStages": []
  }
]
```

</details>


## Debug
```
$ docker inspect spark:3.5.1-scala2.12-java17-python3-ubuntu
$ docker cp spark-docker-compose-spark-master-1:/opt/entrypoint.sh .
```
## Ref
- https://github.com/apache/spark-docker
- https://hub.docker.com/_/spark
- https://github.com/apache/spark-docker/blob/master/OVERVIEW.md#environment-variable
- https://spark.apache.org/docs/latest/spark-standalone.html

### spark + prometheus
- https://stackoverflow.com/questions/49488956/how-to-monitor-apache-spark-with-prometheus
- https://spark.apache.org/docs/3.5.1/monitoring.html
- https://grafana.com/docs/grafana-cloud/monitor-infrastructure/integrations/integration-reference/integration-spark/
- https://dzlab.github.io/bigdata/2020/07/03/spark3-monitoring-1/
- https://github.com/apache/spark/pull/25741
- https://medium.com/@bhavya.joshi1901/monitoring-apache-spark-metrics-with-prometheus-a2846fe94028

### prometheus container Advisor
- https://prometheus.io/docs/guides/cadvisor/#docker-compose-configuration

### prometheus 
- https://github.com/cerndb/spark-dashboard?tab=readme-ov-file

### prometheus client
- https://prometheus.io/docs/instrumenting/clientlibs/