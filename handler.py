import runpod

def handler(job):

    print("Job received")

    return {
        "message": "Worker is running",
        "input": job["input"]
    }

runpod.serverless.start(
    {"handler": handler}
)