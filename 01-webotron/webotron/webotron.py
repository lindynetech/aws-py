import boto3
import click

session = boto3.Session()
s3 = session.resource("s3")

@click.group()
def cli():
    "Deploy S3 website to AWS"
    pass

@cli.command("list-buckets")
def list_buckets():
    "List all s3 buckets"
    for b in s3.buckets.all():
        print(b)

@cli.command("list-bucket-objects")
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
   cli()



