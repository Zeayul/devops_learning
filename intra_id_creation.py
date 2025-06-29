# Code snippets are only available for the latest version. Current version is 1.x
from msgraph import GraphServiceClient
from msgraph.generated.models.user import User
from msgraph.generated.models.password_profile import PasswordProfile
from azure.identity import ClientSecretCredential
import asyncio
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
scopes = ['https://graph.microsoft.com/.default']

tenant_id = ''
client_id = ''
client_secret = ''

# azure.identity
credential = ClientSecretCredential(
    tenant_id,
    client_id,
	client_secret)

graph_client = GraphServiceClient(credential, scopes)

async def create_user():
	request_body = User(
		account_enabled = True,
		display_name = "Anish Pailo",
		mail_nickname = "Apailo",
		user_principal_name = "apailo@devops.zea.com",
		password_profile = PasswordProfile(
			force_change_password_next_sign_in = True,
			password = "xWwv",
		),
	)

	result = await graph_client.users.post(request_body)
	return result


if __name__ == "__main__":
	res = asyncio.run(create_user())
	print(res)