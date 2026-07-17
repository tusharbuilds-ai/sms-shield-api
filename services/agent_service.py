from langchain.agents import create_agent
from prompts.prompt import SYSTEM_PROMPT
from dotenv import load_dotenv


load_dotenv()

agent = create_agent(
    model="google_genai:gemini-2.5-flash",
    system_prompt=SYSTEM_PROMPT,
)


def ai_explaination(message:str,sender:str,classification:str,language:str):
    result = agent.invoke({
    "messages":[{"role":"user", "content":f"""Message received -> {message} , Sent By -> {sender}, SVM model prediction - > {classification}, explanation language -> {language}. Explain only in 80 words."""}]
    })

    return result["messages"][-1].content_blocks[0]["text"]