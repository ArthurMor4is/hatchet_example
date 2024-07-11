
import asyncio
from hatchet_sdk import Hatchet
import logging

logger = logging.getLogger(__name__)

def create(state: str) -> str:
    if state:
        try:
            return asyncio.run(hatchet_test(state))
        except Exception as e:
            logger.debug("Failed to trigger workflow")
            logger.debug(f"Error: {str(e)}")

async def hatchet_test(state: str) -> str:
    hatchet = Hatchet()
    workflow_run = await hatchet.client.admin.aio.run_workflow("BasicRagWorkflow", {"state": state})
    return workflow_run.workflow_run_id

