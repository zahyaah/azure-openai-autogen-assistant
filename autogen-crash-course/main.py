from autogen_agentchat.agents import AssistantAgent 
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient 
from dotenv import load_dotenv
import asyncio 
import os 

async def main():
    load_dotenv()
    # print(os.getenv("AZURE_OPENAI_ENDPOINT"))
    # print(os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"))
    # print(os.getenv("AZURE_OPENAI_API_VERSION"))
    # print(os.getenv("AZURE_OPENAI_KEY"))

    model_client = AzureOpenAIChatCompletionClient(
        model='gpt-4.1-2025-04-14',
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        azure=True
    ) # brain

    assistant = AssistantAgent(name='assistant', model_client=model_client, description='a basic first agent') # giving a "human", the above brain

    result1 = await assistant.run(task="what's the capital of france?")
    print(result1.messages[-1].content)


    result2 = await assistant.run(task="what's the capital of india?")
    print(result2.messages[-1].content)

    await model_client.close()

asyncio.run(main())