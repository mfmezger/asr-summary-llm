"""This is the API for the ASR Summary LLM app."""
import json
import os

import torch
import whisper_timestamped as whisper
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from loguru import logger
from pyannote.audio import Pipeline

load_dotenv()

app = FastAPI()

device = "cuda" if torch.cuda.is_available() else "cpu"


@app.get("/")
async def root():
    """This is the root endpoint."""
    return {"message": "Hello World"}


# Endpoint for the upload of a file
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    """This is the endpoint for the upload of a file."""
    pass


def speaker_diarization(file_name: str):
    """This is the speaker diarization function."""
    logger.info(f"Using Device: {device}")

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization@2.1",
        use_auth_token=os.getenv("HF_TOKEN"),
    )
    pipeline = pipeline.to(torch.device(0))
    DEMO_FILE = {"uri": "blabal", "audio": file_name}
    dz = pipeline(DEMO_FILE)

    # todo: set file name.
    with open("diarization.txt", "w") as text_file:
        text_file.write(str(dz))
    # todo: convert to json and improve output.


def whisper_with_timestamp(file_name: str, model_size: str = "large", language: str = "de"):
    """This is the whisper function."""
    audio = whisper.load_audio(file_name)

    model = whisper.load_model(model_size, device=device)

    result = whisper.transcribe(model, audio, language=language)

    # save result as json file
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    pass
