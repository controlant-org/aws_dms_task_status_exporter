from aws_dms_task_status_exporter.helper import get_conf_file
import boto3
from os import environ


def get_status_replication_tasks(dms_client=boto3.client("dms")):
    conf = get_conf_file()

    result = []
    response = dms_client.describe_replication_tasks(
        Filters=[{"Name": "replication-task-id", "Values": conf["replication-task-id"]}]
    )["ReplicationTasks"]

    for resp in response:
        result.append(
            {
                "replication_task_identifier": resp["ReplicationTaskIdentifier"],
                "status": resp["Status"],
            }
        )

    return result
