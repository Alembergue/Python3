from utils import select
from io import StringIO, BytesIO
import pandas as pd
import requests
import boto3
import gzip




class Client(object):
    """Generates a boto3 client for working with Pandas3"""
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.boto3_session = boto3.client('s3',
                                          aws_access_key_id=aws_access_key_id,
                                          aws_secret_access_key=aws_secret_access_key,
                                          region_name=region_name)

    def list_buckets(self):
        """List all buckets for user"""
        return self.boto3_session.list_buckets()

    def list_files(self, bucket):
        """List all files in a bucket, excluding all `directories`"""
        return [{'File Size': x['Size'],
                 'File Name': x['Key'],
                 'File Type': x['Key'][x['Key'].rfind('.')+1:].upper(),
                 'Last Updated': x['LastModified']}
                for x in self.boto3_session.list_objects(Bucket=bucket)['Contents'] if x['Size'] > 0]

    @staticmethod
    def select_df(self, bucket, file, query, header='Use', format='pandas'):
        """S3 Select returning Pandas dataframe or using SQL query."""
        valid_headers = {'Use', 'None'}
        if header not in valid_headers:
            raise ValueError("headers must be one of %r." % valid_headers)

        #TODO: query and header handling

    def upload_df(self, bucket, df, file_name, compression=True):
        """Upload Pandas Dataframe to S3 storage"""
        # write DF to string stream
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        file = csv_buffer.getvalue()

        if not isinstance(compression, bool):
            raise ValueError("compression variable must be boolean value")

        if compression:
            # reset stream position
            csv_buffer.seek(0)
            # create binary stream
            gz_buffer = BytesIO()

            # compress string stream using gzip
            with gzip.GzipFile(mode='w', fileobj=gz_buffer) as gz_file:
                gz_file.write(bytes(csv_buffer.getvalue(), 'utf-8'))

            file = gz_buffer.getvalue()

        # write stream to S3
        files = {"file": file}

        post = self.boto3_session.generate_presigned_post(
            Bucket=bucket,
            Key=file_name
        )
        response = requests.post(post["url"], data=post["fields"], files=files)

        return response.text if response.text else "Upload Completed"




