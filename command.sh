# Install python package
pip3 install -r requirements.txt

# Produce message to Kafka
python3 produce_message.py

# Spark Submit
docker exec spark-master bash -c "python3 /opt/workspace/spark_stream.py"

# Query cassandra
docker exec -it cassandra cqlsh -u cassandra -p cassandra localhost 9042
select * from spark_streams.created_users;

select first_name, last_name from spark_streams.created_users;