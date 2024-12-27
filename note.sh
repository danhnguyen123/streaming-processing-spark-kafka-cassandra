docker exec -it spark-master spark-submit /opt/workspace/spark_stream.py
docker exec -it cassandra cqlsh -u cassandra -p cassandra localhost 9092