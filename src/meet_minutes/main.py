#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start
from crews.meeting_minutes.meeting_minutes_crew import MeetingMinutesCrew
from crews.mailcrew.mailcrew import Mailcrew
from dotenv import load_dotenv
from openai import OpenAI
from pydub import AudioSegment
from pydub.utils import make_chunks

load_dotenv()
client = OpenAI()
class MeetMinutesState(BaseModel):
    transcript: str = ""
    summary: str = ""


class MeetMinutesFlow(Flow[MeetMinutesState]):

    @start()
    def transcribe_meeting(self):
        print("Generating transcript")

        audio = r"C:\Users\edafe\Downloads\Analysis of the Gift of Tongues.wav"
        segment = AudioSegment.from_file(audio, format="wav")
        chunks = make_chunks(segment, 60000)

        full_transcription = ""

        for i, chunk in enumerate(chunks):
            print(f"Transcribing {i+1}/{len(chunks)}")
            chunk_path = f"chunk_{i}.wav"
            chunk.export(chunk_path, format="wav")

            with open(chunk_path, "rb") as c:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=c


                )

                full_transcription += transcription.text + ""
        self.state.transcript = full_transcription
        print(self.state.transcript)

    @listen(transcribe_meeting)
    def generate_minutes(self):
        print("Generating transcript")

        crew = MeetingMinutesCrew()
        inputs = {"transcript": self.state.transcript}

        minutes = crew.crew().kickoff(inputs)
        self.state.summary = minutes

    @listen(generate_minutes)
    def write_draft_minutes(self):
        print("Writing minutes")
        crew = Mailcrew()

        inputs = {"body": self.state.summary}

        draft = crew.crew().kickoff(inputs)


def kickoff():
    meet_minutes_flow = MeetMinutesFlow()
    meet_minutes_flow.plot()
    meet_minutes_flow.kickoff()


def plot():
    meet_miuntes_flow = MeetMinutesFlow()
    meet_miuntes_flow.plot()


if __name__ == "__main__":
    kickoff()
