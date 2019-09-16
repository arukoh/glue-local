import sys
from awsglue.transforms import ApplyMapping
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

DYNAMODB_INPUT_TABLE_NAME = 'examples-table'
S3_OUTPUT_BUCKET_NAME = 'examples-bucket'

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
JOB_NAME = args['JOB_NAME']

sc = SparkContext()
glueContext = GlueContext(sc)
job = Job(glueContext)
job.init(JOB_NAME, args)

datasource = glueContext.create_dynamic_frame.from_options(
    connection_type='dynamodb',
    connection_options={
        'dynamodb.input.tableName': DYNAMODB_INPUT_TABLE_NAME
    }
)

applymapping = ApplyMapping.apply(
    frame=datasource,
    mappings=[
        ('Id', 'string', 'Id', 'string'),
        ('Column1', 'string', 'Column1', 'string'),
        ('Column2', 'string', 'Column2', 'string'),
        ('Column3', 'string', 'Column3', 'string')
    ]
)

glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type='s3',
    connection_options={
        'path': 's3://' + S3_OUTPUT_BUCKET_NAME
    },
    format='csv'
)

job.commit()
