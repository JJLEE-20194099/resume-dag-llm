sudo docker run -d \
--name es-container \
--net es-net \
-p 9201:9201 \
-e xpack.security.enabled=false \
-e discovery.type=single-node \
docker.elastic.co/elasticsearch/elasticsearch:7.11.0


sudo docker run -d --name kb-container --net es-net -p 5602:5602 -e ELASTICSEARCH_HOSTS=http://es-container:9200 docker.elastic.co/kibana/kibana:7.11.0