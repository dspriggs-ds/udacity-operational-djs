
import json
import os
import azureml.core
from azureml.core import Workspace
from azureml.core.webservice import Webservice
from azureml.core.authentication import ServicePrincipalAuthentication

os.chdir('/home/dspriggs/workdir/python/nd00333_AZMLND_C2/starter_files')

svc_pr_password = "DYhFqFue.e-8k9owE.79Hj23Sk9~.EHFc4"

svc_pr = ServicePrincipalAuthentication(
    tenant_id="2d90ae77-89d8-461b-ad0c-86bb90791242",
    service_principal_id="c743064a-78c0-403e-b478-1b342bf91073",
    service_principal_password=svc_pr_password)


ws = Workspace(
    subscription_id="7ed88a19-c34d-46ea-b174-03230033a976",
    resource_group="djslearning",
    workspace_name="djsudacity",
    auth=svc_pr
    )

mlservice ="djsbestmodel"

web_service=Webservice(mlservice, ws)

web_service.update(enable_app_insights=True)

logs = web_service.get_logs()

for line in logs.split('\n'):
    print(line)


