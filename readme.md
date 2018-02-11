### Setup

Welcome to a simple [serverless blog](https://serverlessblog.com/). You can:
- [Copy this project](https://github.com/bearword/bearword/wiki/Forking) for use with your own [AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services) endpoints. 
- Or, just [start contributing to this project](https://github.com/bearword/bearword/wiki/Contributing)!

When done with either setup, you can start development.

### Development

#### Install DynamoDB

If `java version` does not show a Runtime Environment `>=6.0`, [install java](https://www.java.com/en/download/), then download DynamoDB:

```
wget -qO- https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz | tar xvz -C lib/dynamodb
```

#### Run locally

In one shell session, start the database like this:

```
java -Djava.library.path=./lib/dynamodb/DynamoDBLocal_lib -jar lib/dynamodb/DynamoDBLocal.jar -sharedDb
```

In another shell session, start the app like this:
```
export BEWO_DYNAMO="http://localhost:8000"
export FLASK_APP="blog.py"
flask run
```

### Deployment

When ready, go ahead and deploy to the dev stage!

```
zappa update dev
```
