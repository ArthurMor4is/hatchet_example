
import asyncio
from hatchet_sdk import Hatchet
import logging

logger = logging.getLogger(__name__)

hatchet = Hatchet()

async def create(state: str) -> str:
    if state:
        try:
            workflow_run = await hatchet.client.admin.aio.run_workflow("BasicRagWorkflow", {"state": state})

            return workflow_run.workflow_run_id
        except Exception as e:
            logger.debug("Failed to trigger workflow")
            logger.debug(f"Error: {str(e)}")
            raise e