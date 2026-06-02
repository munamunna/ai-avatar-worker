import runpod
import edge_tts

from cloudinary_service import upload_audio


async def generate_audio(text):

    output_file = "speech.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save(output_file)

    return output_file


async def handler(job):

    text = job["input"]["text"]

    audio_file = await generate_audio(text)

    audio_url = upload_audio(audio_file)

    return {
        "audio_url": audio_url
    }


runpod.serverless.start(
    {"handler": handler}
)