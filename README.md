# Meet Minutes Project

## Overview

The Meet Minutes project is designed to facilitate the automated transcription, summarization, and distribution of meeting minutes. Leveraging a multi-agent AI system powered by crewAI, this project streamlines the process of converting audio recordings of meetings into actionable insights and organized minutes.

## Features

- **Audio Transcription**: Utilizes the OpenAI Whisper model to transcribe meeting audio files into text.
- **Minutes Generation**: Summarizes the transcribed text into concise meeting minutes, capturing key discussion points and action items.
- **Email Drafting**: Automatically drafts emails with the meeting summary for easy distribution.
- **Sentiment Analysis**: Analyzes the sentiment of the meeting discussion, providing insights into the tone and mood of the conversation.
- **Action Item Tracking**: Identifies and compiles action items for follow-up and accountability.

## Components

- **MeetMinutesFlow**: Manages the flow of data from transcription to minutes generation and email drafting.
- **MeetingMinutesCrew**: A crew of AI agents responsible for summarizing and writing the meeting minutes.
- **Mailcrew**: A crew focused on handling email-related tasks, such as drafting and sending emails through Gmail utilities.
- **Custom Tools**: Includes tools for file writing and email creation, integrated with Google Gmail APIs for seamless communication.


## Customization

- Configure agents in `src/meet_minutes/config/agents.yaml`.
- Define tasks in `src/meet_minutes/config/tasks.yaml`.
- Modify `src/meet_minutes/crew.py` and `src/meet_minutes/main.py` for custom logic and inputs.

## Support

For support or questions, just give the project a star

## License

This project is licensed under the MIT License.