import cloudinary
import cloudinary.uploader
import os

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

def upload_audio(audio_path):

    result = cloudinary.uploader.upload(
        audio_path,
        resource_type="video",
        folder="audio"
    )

    return result["secure_url"]