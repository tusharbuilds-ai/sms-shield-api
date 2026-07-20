from langchain.agents import create_agent
from prompts.prompt import SYSTEM_PROMPT,ANALYTICS_SYSTEM_PROMPT
from dotenv import load_dotenv


load_dotenv()

agent = create_agent(
    model="google_genai:gemini-2.5-flash",
    system_prompt=SYSTEM_PROMPT,
)

analytics_angent = create_agent(
    model="google_genai:gemini-2.5-flash",
    system_prompt=ANALYTICS_SYSTEM_PROMPT,
)

def ai_analytics(message:list[str],sender:list[str],timestamp:list[int]):
    result = analytics_angent.invoke({
        "messages":[{
            "role":"user",
            "content":f"""Messages received - > {message}
            Sent by - > {sender}
            Timestamp - > {timestamp}
            """
        }]
    })

    return result["messages"][-1].content_blocks[0]["text"]
        


def ai_explaination(message:str,sender:str,classification:str,language:str):
    result = agent.invoke({
    "messages":[{"role":"user", "content":f"""Message received -> {message} , Sent By -> {sender}, SVM model prediction - > {classification}, explanation language -> {language}. Explain only in 80 words."""}]
    })

    return result["messages"][-1].content_blocks[0]["text"]