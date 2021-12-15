import json
import boto3
def lambda_handler(event, context):
    if event:
        try:
            s3_client = boto3.client("s3")
            s3_resource = boto3.resource('s3')
            bucket = event['Records'][0]['s3']['bucket']['name']
            fileKey = event['Records'][0]['s3']['object']['key']
            try:
                copy_src = {
                    'Bucket': bucket,
                    'Key': fileKey
                }
                backup_bucket_name = 'bucket-backup' # change this bucket name to your back up bucket
                destination_bucket = s3_resource.Bucket(backup_bucket_name)
                newFileName = str(fileKey) + '-backup'
                destination_bucket.copy(copy_src,newFileName)
            except Exception as e:
                print(e)
                print('Failure to copy the object to the destination bucket')
            else:
                print('the file ' + fileKey + ' has been copied succefully to the bucket ' + backup_bucket_name )
        except Exception as e:
            print(e)
            print('Error could not find the object in the specified bucket!')