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

    def publish_message(topic, message, attributes):
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
            att_dict = {}
            for key, value in attributes.items():
                if isinstance(value, str):
                    att_dict[key] = {
                        'DataType': 'String', 'StringValue': value}
                elif isinstance(value, bytes):
                    att_dict[key] = {
                        'DataType': 'Binary', 'BinaryValue': value}
            response = topic.publish(
                Message=message, MessageAttributes=att_dict)
            message_id = response['MessageId']
            logger.info(
                "Published message with attributes %s to topic %s.", attributes,
                topic.arn)
        except ClientError:
            logger.exception(
                "Couldn't publish message to topic %s.", topic.arn)
            raise
        else:
            return message_id


def lambdaHandler(event, context):
    notification = SnsWrapper()
    notification()
