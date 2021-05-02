import boto3


def get_db():
    dynamodb = boto3.resource("dynamodb")
    return dynamodb


def get_movies_table():
    db = get_db()
    return db.Table("movies")
