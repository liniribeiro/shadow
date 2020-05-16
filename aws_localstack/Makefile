sqs-bts-queue:
	aws sqs create-queue --endpoint-url=http://localhost:4576 --queue-name shadow-bts-local

sqs-ui-queue:
	aws sqs create-queue --endpoint-url=http://localhost:4576 --queue-name shadow-ui-local


sns-kpop-topic:
	aws sns create-topic --endpoint-url=http://localhost:4575 --name shadow-kpop-local \
	&& make sqs-bts-queue \
	&& make sqs-ui-queue \
	&& aws sns subscribe --endpoint-url=http://localhost:4575 --topic-arn arn:aws:sns:us-east-1:000000000000:shadow-kpop-local --protocol sqs --notification-endpoint arn:aws:sqs:us-east-1:000000000000:shadow-ui-local --attribute-name "FilterPolicy" --attribute-value "{\"channel\":\"ui\"}" \
	&& aws sns subscribe --endpoint-url=http://localhost:4575 --topic-arn arn:aws:sns:us-east-1:000000000000:shadow-kpop-local --protocol sqs --notification-endpoint arn:aws:sqs:us-east-1:000000000000:shadow-bts-local --attribute-name "FilterPolicy" --attribute-value "{\"channel\":\"bts\"}"
