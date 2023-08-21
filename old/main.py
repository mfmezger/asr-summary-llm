"""MAIN."""
import torch
from pyannote.audio import Pipeline

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)


def main():
    """Main."""
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization@2.1",
        use_auth_token="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",
    )
    pipeline = pipeline.to(torch.device(0))
    DEMO_FILE = {"uri": "blabal", "audio": "audio.wav"}
    dz = pipeline(DEMO_FILE)

    with open("diarization.txt", "w") as text_file:
        text_file.write(str(dz))


if __name__ == "__main__":
    main()
