import runpod
import asyncio
import edge_tts


async def generate_audio(text):

    output_file = "speech.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save(output_file)

    return output_file


def handler(job):

    text = job["input"]["text"]

    audio_file = asyncio.run(
        generate_audio(text)
    )

    return {
        "audio_file": audio_file
    }


runpod.serverless.start(
    {"handler": handler}
)