import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from root_agent import root_agent


async def main():

    session_service = InMemorySessionService()

    runner = Runner(
        agent=root_agent,
        session_service=session_service,
        app_name="maintenance_ai"
    )

    session = await session_service.create_session(
        app_name="maintenance_ai",
        user_id="alae"
    )

    while True:

        question = input("\nMachine : ")

        if question.lower() == "exit":
            break

        async for event in runner.run_async(
        user_id="alae",
        session_id=session.id,
        new_message=question
):
    print(event)

        print("\n========================")
        print(response)
        print("========================\n")


if __name__ == "__main__":
    asyncio.run(main())