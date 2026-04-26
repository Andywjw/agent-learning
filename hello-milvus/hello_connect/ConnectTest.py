from pymilvus import MilvusClient, DataType

# 创建数据库
client = MilvusClient(
    uri="http://localhost:19530",
    token="root:Milvus"
)

# client.create_database(
#     db_name="my_database_1"
# )

client.create_database(
    db_name="my_database_2",
    properties={
        "database.replica.number": 3
    }
)

client.list_databases()

# Output
# ['default', 'my_database_1', 'my_database_2']

# Check database details
client.describe_database(
    db_name="default"
)


client.use_database(
    db_name="my_database_2"
)

client = MilvusClient(
    uri="http://localhost:19530",
    token="root:Milvus"
)

# 3.1. Create schema
schema = MilvusClient.create_schema(
    auto_id=False,
    enable_dynamic_field=True,
)

# 3.2. Add fields to schema
schema.add_field(field_name="my_id", datatype=DataType.INT64, is_primary=True)
schema.add_field(field_name="my_vector", datatype=DataType.FLOAT_VECTOR, dim=5)
schema.add_field(field_name="my_varchar", datatype=DataType.VARCHAR, max_length=512)