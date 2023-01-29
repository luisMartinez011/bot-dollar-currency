# bot-dollar-currency
I want to buy an AWS certification exam but it is only available in USD dollars, so I build this bot to track the USD - MXN exchange and emailing me once per day to check when it is the best opportunity to buy the exam. 


## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.
* ExchangeRate API - [Get an api key here](https://www.exchangerate-api.com)
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build 
sam deploy --guided
```

There are two environment variable in template.yaml

```yaml
      Environment:
        Variables:
          API_KEY: YOUR_API_KEY
```

```yaml
      BDCEventbridge:
          Type: AWS::Scheduler::Schedule
          Properties:
            Description: "Timer for bot dollar currency"
            FlexibleTimeWindow:
              Mode: "OFF"
            ScheduleExpression: "cron(0 12 * * ? *)"
            Target:
              Arn: !GetAtt FlowChart.Arn
              RoleArn: Your_Role_ARN
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name bot-dollar-currency
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
