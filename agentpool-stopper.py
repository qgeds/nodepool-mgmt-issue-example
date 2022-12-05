from azure.common.credentials import ServicePrincipalCredentials
from azure.identity import DefaultAzureCredential
from azure.mgmt.containerservice import ContainerServiceClient, models

resource_group_name = '#'
cluster_name = '#'
node_pool_name = '#'
subscription_id = '#'

credentials = DefaultAzureCredential()
client = ContainerServiceClient(credentials, subscription_id)

pool = client.agent_pools.get(resource_group_name, cluster_name, node_pool_name)
pool.power_state=models.PowerState(code="Stopped")

poller = client.agent_pools.begin_create_or_update(
    resource_group_name,
    cluster_name,
    node_pool_name,
    pool)
sc_result = poller.result()