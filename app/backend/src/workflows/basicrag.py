import asyncio
from .hatchet import hatchet
from hatchet_sdk import Context
from ..api_hatchet.service import create
import time
@hatchet.workflow()
class BasicRagWorkflow:
    @hatchet.step()
    async def call_children(self, context: Context):
        state = context.input.get("state")
        print(f"{state}: Initializing workflow at time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        await asyncio.sleep(10)
        if state == "initial":
            next_state = "children"
        elif state == "children":
            next_state = "children2"
        else:
            next_state = None

        child_workflow_run_ids = []
        if next_state:
            for _ in range(5):                
                child_workflow_run = await context.aio.spawn_workflow(
                    "BasicRagWorkflow", {"state": next_state}
                )

                child_workflow_run_ids.append(child_workflow_run.workflow_run_id)
        
        print(f"{state}: Finished call_children at time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        return {"child_workflow_run_ids": child_workflow_run_ids}
    
    @hatchet.step(parents=["call_children"])
    async def wait_for_children(
        self, context: Context
    ):
        state = context.input.get("state")
        print(f"{state}: Waiting for children at time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        child_workflow_run_ids = context.step_output("call_children")["child_workflow_run_ids"]

        results = []
        for id in child_workflow_run_ids:
            results.append(await hatchet.client.admin.get_workflow_run(id).result())

        is_done = all(result["wait_for_children"]["done"] is True for result in results)

        if not is_done:
            raise Exception("Some child workflows could not finish.")

        print(f"{state}: Finished waiting for children at time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
        return {"done": True}
