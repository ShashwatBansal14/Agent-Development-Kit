import uuid
import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from question_answering_agent.agent import question_answering_agent

load_dotenv()


async def main():
    # Create a new session service
    session_service_stateful = InMemorySessionService()

    initial_state = {
        "user_name": "Shashwat Bansal",
        "user_preferences": """
        I like to play basketball, BGMI, PC games, and badminton.
        My favorite food is Indian.
        My favorite TV show is Loki.
        Loves it when people appreciate gaming skills.
        """,
    }

    APP_NAME = "Shashwat Bot"
    USER_ID = "Shashwat_bansal"
    SESSION_ID = str(uuid.uuid4())

    
    await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )

    print("CREATED NEW SESSION:")
    print(f"\tSession ID: {SESSION_ID}")

    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )

    new_message = types.Content(
        role="user",
        parts=[types.Part(text="What is Shashwat's favorite TV show?")],
    )

    # Runner handles async internally
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response: {event.content.parts[0].text}")

    print("==== Session Event Exploration ====")

    
    session = await session_service_stateful.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    print("=== Final Session State ===")
    for key, value in session.state.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
