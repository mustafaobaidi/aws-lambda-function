# aws-lambda-function
A serverless function that is triggered when a new file is added to one of the  storage buckets (S3).
In response to the trigger a log entry is made on an appropriate logfile ( I use CloudWatch).
The file is copied to a backup bucket.
