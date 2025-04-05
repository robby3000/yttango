---
title: "Yttango Project Spec"
date: 2025-04-04
draft: false
description: "Organized YouTube Transcripts"
tags: ["youtube", "transcripts"]
categories: ["general", "youtube", "transcripts"]
---

**Product Specification: YouTube Playlist Manager AKA Yttango**  

---

### **Product Overview**  
A web app named Yttango designed for personal use to help efficiently assess the content of videos from YouTube playlists and channels by providing AI-generated summaries, metadata, and export tools. Selected videos arecan either be output as a list of URLs, for example for adding to a NotebookLM or other RAG system, or they can be added to a playlist on your Youtube channel.

**Note:** The user can add video URLs individually, or can add the URLs of Youtube channels or playlists in which case the app will generate an RSS feed URL for each channel or playlist, and then list and extract the contents of the most recent 15 videos of the feed (or any new videos that the app has not already processed, up to a maximum of 15 which is the limit for videos in Youtube feeds).

---

### **Key Features**  
1. **AI Summaries**  
   - Generate summaries for each video in a playlist or channel by extracting the transcript and passing it to an LLM such as Gemini 2.0 to create the summaries.  


**Functional Requirements**
   - Contents stored in a SQLite database locally.
   - User can delete database entries or purge the entire database. 
   - User runs the extension periodically when needed and the extension only adds new videos to the database.
   - User has the option to manually add videos to the database.
   - User can update the summary for each video.
   - User can delete videos from the database.
   - User can export the database to a CSV file.
   - User can import a CSV file to the database, or export selected entries as a .csv
   - CSS styling is in typical dark mode.

2. **Metadata Display**  
   - Show title, channel name, video length, video description, and date for each video.  

3. **Accordion Transcriptions**  
   - Expandable drawer for each video to view full transcription.

4. **Checkbox Selection**  
   - Users can select videos to export via checkboxes. 

5. **Export Functionality**  
   - Export selected video URLs to a list.  
   - Include a “Copy to Clipboard” button for each URL.  

6. **Share URL**  
   - Generate a shareable link for the curated playlist.  

---

### **Technical Requirements**  
1. **API Integration**  
   - Use **YouTube Data API v3** to fetch playlist data, video metadata,  
   - Ensure compliance with YouTube’s API terms (e.g., quotas, attribution).  

2. **AI Integration**  
   - Integrate an AI service (e.g., Google Gemini 2.0) for summarization.  

3. **App Architecture**  
   - The 1st stage MVP is already done, in the yttango directory projects/yttango. This is a simple python application of the youtube-transcript-api that provides the transcript for a given Youtube URL. 
   - For Youtube playlist and channel feed URLs that the user enters the app extracts the video URLs. A user can also add individual video URLs. 
   - Uses the Youtube data API v3 to extract the required metadata.
   - Uses the youtube-transcript-api to extract the transcripts.
   - Passes the transcripts to Gemini 2.0 LLM for processing to produce the summaries and key takeaways.
   - Build using HTML/CSS/flask/python and maybe some javascript if required.  
   - Store user preferences locally (e.g., selected playlists, channels).  
   - User can export selected videos in 2 ways: 1. adding to a playlist in their Youtube account, or 2. listing chosen selected videos with each one having a 'copy URL to clipboard' button.
   - When a user adds a Youtube channel the app creates the 
   - There is a 'load videos' button that processes the latest 15 videos from each channel and playlist feed, as well as any individual videos that the user adds (via a '+ video' button).

4. **UI/UX**  
   - Clean, minimal interface. 
   - Responsive design for mobile and desktop.  

---

### **User Interface (UI) Design**  
1. **Playlist Selection**  
   - Users paste in a URL of a Youtube playlist or channel. 

2. **Video List View**  
   - Display videos in a grid/list with metadata and details 
   - Include checkboxes for selection to have their URLs exported.  

3. **Summary & Score**  
   - Show AI-generated summary for each video.  

4. **Accordion Transcription**  
   - Expandable section to view full transcription (if available).  

5. **Export Panel**  
   - Button to export selected URLs.  
   - List of URLs with copy-to-clipboard buttons.  

---

### **Compliance & Legal**  
1. **YouTube API Terms**  
   - Adhere to **Requirements for Minimum Functionality (RMF)** (e.g., no removal of YouTube branding).  
   - Display YouTube’s Terms of Service link in the extension.  
   - Avoid redistributing copyrighted content (transcriptions are for personal use only).  

2. **Data Privacy**  
   - It's for personal use only, no data is collected or shared.  

3. **Attribution**  
   - Not necessary to attribute AI summaries as machine-generated. 

---

### **Development Roadmap**  
1. **Phase 1: Core Features**  
   - Playlist selection, metadata display, AI summaries, export functionality.  

2. **Phase 2: UI/UX Enhancements**  
   - Improve transcription display, add sorting/filtering options.  

3. **Phase 3: Compliance & Testing**  
   - Audit for YouTube API compliance, user testing, and Chrome Web Store submission.  

---

### **Testing Considerations**  
- **Unit Tests:** Validate AI summarization accuracy and API response handling.  
- **Integration Tests:** Ensure seamless interaction with YouTube’s API and Gemini LLM api. 
- **User Testing:** Gather feedback on UI/UX and export functionality.  

---

