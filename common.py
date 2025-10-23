from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from dotenv import load_dotenv
import os
from autogen_ext.models.azure import AzureAIChatCompletionClient

class LLM:
    def __init__(self):
        load_dotenv()
        self.az_token=os.getenv('AZURE_OPENAI_API_KEY')
        self.az_url=os.getenv('AZURE_OPENAI_BASE_URL')
        self.az_ver =os.getenv('AZURE_OPENAI_API_VERSION')         
        self.az_embed = os.getenv('AZURE_OPENAI_EMBEDDING_DEPLOYMENT') 
        self.az_model = os.getenv('AZURE_OPENAI_MODEL')

    @property
    def _model(self) -> AzureOpenAIChatCompletionClient:
        return AzureOpenAIChatCompletionClient(
            api_key=self.az_token,
            azure_deployment=self.az_model,
            api_version=self.az_ver,
            model=self.az_model,
            azure_endpoint=self.az_url
        )
    @property
    def llm_client(self) -> AzureOpenAIChatCompletionClient:
        return AzureOpenAIChatCompletionClient( 
        api_key=self.az_token,
        azure_deployment="gpt-4.1",
        api_version="2024-12-01-preview",
        model="gpt-4.1",
        azure_endpoint="https://somazopenaikey.openai.azure.com/"
    )
    
    
class MCPActions:
    def __init__(self):
        load_dotenv()
        self.MCP_Actions = os.getenv('MCP_API_Actions')

    def get_mcp_actions(self)->list[str]:
        return self.MCP_Actions.split(',')


