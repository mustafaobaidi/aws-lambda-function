# aws-lambda-function
A serverless function that is triggered when a new file is added to one of the  storage buckets (S3).
In response to the trigger a log entry is made on an appropriate logfile ( I use CloudWatch).
The file is copied to a backup bucket.



Steps to test the functionality:
------------------------------------
1- We need to create two buckets. The first bucket is the bucket that will we be adding the files to, and the second bucket is going to be our backup. For example, first bucket: cis4010-username and second bucket: cis4010-username-backup.

2- create a role that you will have access too.

3- Create a lambda function and choose 'the role you created' as an existing role.

4- click on the lambda function that you have created and select configuarion, and choose add trigger from configuration. Select S3  from the drop down menu and choose your main bucket. When you are done click add. This process aims to configure your lambda function with your bucket, as whenever an event happens in the bucket the lambda function will be triggered. Please note that you need to make sure that the bucket you are choosing have not been configured before with another lambda function.

5- You can now test this by adding a file to the configured bucket. When you are done uploading the file, go to the cloudWatch, then log groups. Notice how you will find a new log group created with the same name as the lambda function. From this log group you can see all the results and what is happening in with the lambda function, wheter it failed or it succedded.

6- after you have added the file to the main bucket, you can now check to see that there have been created a backup bucket for you with the same name as you main bucket and appending '-backup' to the name. Notice how the file you uploaded in the main bucket have been copied to the backup bucket.

7- You can also upload multiple files and the lambda function will copy them all with no problem. However, that will be conisdered as multiple requests and not one request.
------------------------------------
