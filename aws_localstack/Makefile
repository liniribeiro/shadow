sqs-bts-queue:
	aws sqs create-queue --endpoint-url=http://localhost:4576 --queue-name shadow-bts-local

sqs-ui-queue:
	aws sqs create-queue --endpoint-url=http://localhost:4576 --queue-name shadow-ui-local


sns-kpop-topic:
	aws sns create-topic --endpoint-url=http://localhost:4575 --name shadow-kpop-local \
	&& make sqs-bts-queue \
	&& make sqs-ui-queue