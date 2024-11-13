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

