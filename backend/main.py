from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp
from moviepy.editor import VideoFileClip
import os
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/clip")
def clip_youtube(url: str = Form(...)):
    video_id = str(uuid.uuid4())
    video_path = f"{OUTPUT_DIR}/{video_id}.mp4"

    # Download YT Video
    ydl_opts = {
        "format": "mp4",
        "outtmpl": video_path
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Load video
    clip = VideoFileClip(video_path)
    duration = clip.duration

    # AUTO CUT → Simple: potong setiap 20 detik
    segment_length = 20
    clips = []

    for i in range(0, int(duration), segment_length):
        start = i
        end = min(i + segment_length, duration)
        out_path = f"{OUTPUT_DIR}/{video_id}_{start}-{end}.mp4"
        sub = clip.subclip(start, end)
        sub.write_videofile(out_path, codec="libx264")
        clips.append(out_path)

    clip.close()

    return {"clips": clips}
