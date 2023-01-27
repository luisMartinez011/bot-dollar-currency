import json
import logging
import time
import boto3
from botocore.exceptions import ClientError
import os


snsTopicArn = os.environ["SNS_TOPIC_ARN"]
logger = logging.getLogger(__name__)


# snippet-start:[python.example_code.sns.SnsWrapper]
class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource

    def publish_message(topic, message):
        """
        Publishes a message, with attributes, to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.
        :param topic: The topic to publish to.
        :param message: The message to publish.
        :param attributes: The key-value attributes to attach to the message. Values
                            must be either `str` or `bytes`.
        :return: The ID of the message.
        """
        try:
            response = topic.publish(
                Message=message,)
            message_id = response['MessageId']
            logger.info(
                "Published message with attributes %s to topic %s.",
                topic.arn)
        except ClientError:
            logger.exception(
                "Couldn't publish message to topic %s.", topic.arn)
            raise
        else:
            return message_id


def lambdaHandler(event, context):
    # message = {"foo": "bar"}

    # client = boto3.client('sns')
    # response = client.publish(
    #     TopicArn=snsTopicArn,
    #     Message=json.dumps({'default': json.dumps(message)}),
    #     MessageStructure='json'
    # )
    return 4
