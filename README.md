## Hatchet Python Example

### Step-by-Step Guide

1. **Start Services**:
   ```sh
   docker compose up postgres redis hatchet-lite
   ```

2. **Navigate to Backend**:
   ```sh
   cd app/backend
   ```

3. **Install Dependencies**:
   ```sh
   poetry install
   ```

4. **Activate Virtual Environment**:
   ```sh
   poetry shell
   ```

5. **Configure Environment**:
   Edit the `.env` file to set `HATCHET_CLIENT_TOKEN` and `HATCHET_CLIENT_TLS_STRATEGY`: [doc link](https://docs.hatchet.run/self-hosting/hatchet-lite#accessing-hatchet-lite)

6. **Run Hatchet Service**:
   ```sh
   poetry run hatchet
   ```

7. **Start API Service**:
   ```sh
   poetry run api
   ```

8. **Send Test Message**:
   ```sh
   curl -X POST http://localhost:8000/message -H "Content-Type: application/json" -d '{"message": ""}'
   ```

### Project Objective

The main objective of this project is to create an API that is defined synchronously and integrated with Hatchet. We aim to ensure that our workflows can wait for the completion of other workflows. Each workflow processes documents, and in some cases, the processing of a document may generate additional documents, leading to the creation of new workflows. This process continues until a document reaches a state that prevents the creation of further "child" documents.


### Error (hatchet worker) when runing the project:

````
initial: Initializing workflow at time: 2024-07-11 11:34:44
Exception in callback PollerCompletionQueue._handle_events(<_UnixSelecto...e debug=False>)()
handle: <Handle PollerCompletionQueue._handle_events(<_UnixSelecto...e debug=False>)()>
Traceback (most recent call last):
  File "/Users/mateusbezrutchka/.asdf/installs/python/3.11.7/lib/python3.11/asyncio/events.py", line 80, in _run
    self._context.run(self._callback, *self._args)
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/completion_queue.pyx.pxi", line 147, in grpc._cython.cygrpc.PollerCompletionQueue._handle_events
BlockingIOError: [Errno 35] Resource temporarily unavailable
````
