from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io


def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition
    Args: local_file_path Path to local audio file, e.g. /path/audio.wav
    Returns: Transcript
    """

    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }

    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print("Transcript: {}".format(alternative.transcript))


# [END speech_transcribe_sync]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local_file_path", type=str, default="resources/brooklyn_bridge.raw"
    )
    args = parser.parse_args()

    sample_recognize(args.local_file_path)


if __name__ == "__main__":
    main()
