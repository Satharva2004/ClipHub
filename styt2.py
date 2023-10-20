import streamlit as st
from pytube import YouTube

st.write(
    """
    # 🎬 ClipHub!
    Download 📲 . Enjoy Free of ads 🔥..."""
)
st.write("")
st.write("")
st.write("")
st.write("")
url = st.text_input("**📌 Enter YouTube URL:**", "URL here 🔗")

if url:
    try:
        my_video = YouTube(url)
        st.write("")
        st.write("## Title:", my_video.title,)
        st.write("")
        st.image(my_video.thumbnail_url)
        video_streams = my_video.streams.filter(progressive=True)
        selected_stream = None
        for stream in video_streams:
            if stream.resolution == "720p":
                selected_stream = stream
                break

        if selected_stream:
            filename = f"{selected_stream.title}.mp4"
            with st.spinner("Creating download link... 🏃💨"):
                download_link = selected_stream.url
                st.markdown(
                    f"Download your video: [Download {filename}]({download_link})"
                )
                st.success("Download link generated successfully! 🤯")
        else:
            st.error("No 720p stream found for this video.")
    except Exception as e:
        st.write("")
        st.write("")
        st.write("")
        st.write("good to go...")
