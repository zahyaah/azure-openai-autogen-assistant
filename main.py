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
    ) 

    assistant = AssistantAgent(name='assistant', model_client=model_client, description='a basic first agent')

    result1 = await assistant.run(task="what's the name of the actor who played Sonny in the movie Bronx Tale?")
    print(result1.messages[-1])


    result2 = await assistant.run(task="who was the protagonist in the movie scarface?")
    print(result2.messages[-1])

    await model_client.close()

asyncio.run(main())