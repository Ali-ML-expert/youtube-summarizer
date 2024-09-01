# 🚀 YouTube AI Summary App

## 📋 Pages and Features

1. 🏠 Home Page
   - Welcome message
   - Brief app description
   - Quick links to other pages

2. 🔐 Authentication
   - Login page
   - Register page
   - Logout functionality

3. 🔍 Search Page
   - Input field for subject/topic
   - Button to initiate YouTube scraping
   - Display of search results with video thumbnails

4. 📊 Results Page
   - List of scraped YouTube videos
   - Thumbnails, titles, and brief descriptions
   - Option to generate summaries for selected videos

5. 📝 Summary Page
   - Display of video summary
   - Short description of the video
   - Bullet points of key takeaways
   - Video thumbnail

6. 🎥 Single Video Summary
   - Input field for YouTube video URL
   - Button to generate summary
   - Display of summary results

7. 📚 History Page
   - List of previously searched topics
   - List of previously summarized videos
   - Option to view past summaries

8. 👤 User Profile
   - User information
   - Settings and preferences

## 🛠️ Technical Requirements

- Django backend
- React.js frontend
- Bootstrap for responsive design
- SQLite database
- Pipenv for dependency management
- Groq API integration for summarization
- ChromaDB and LangChain for data processing
- YouTube scraping functionality
- Groq embeddings and model API calls
- React CoT or similar frameworks for enhanced UI

## 🔧 Core Functionalities

1. 🕷️ YouTube Scraping
   - Scrape top results from YouTube for a given subject
   - Focus on videos from the recent week
   - Store scraped URLs in SQLite database

2. 🤖 AI Summarization
   - Use Groq API to summarize YouTube videos
   - Generate short descriptions and key points
   - Process both multiple videos from search and single video URLs

3. 🖼️ Image Display
   - Show thumbnails for each summarized video

4. 🔒 User Authentication
   - Implement secure login and registration system

5. 📱 Responsive Design
   - Ensure app is fully responsive across devices

6. 🧠 AI-Enhanced Features
   - Utilize ChromaDB and LangChain for advanced data processing
   - Implement Groq embeddings for improved summarization

## 🎯 Next Steps

1. Set up Django project structure
2. Configure React.js frontend
3. Implement authentication system
4. Develop YouTube scraping functionality
5. Integrate Groq API for summarization
6. Design and implement responsive UI
7. Set up database models and storage
8. Implement history and user profile features
9. Thorough testing and refinement

## Project Components

1. **YoutubeSummarizer/** (Project root)
   - Contains project-wide settings and configuration

2. **summarizer/** (Main application)
   - Contains the core functionality of the YouTube summarizer

3. **templates/**
   - HTML templates for rendering views

4. **static/**
   - CSS, JavaScript, and other static files

5. **migrations/**
   - Database migration files

## Key Files

- **settings.py**: Project settings and configuration
- **urls.py**: URL routing for the project and app
- **views.py**: View functions/classes for handling requests
- **models.py**: Database models
- **forms.py**: Form definitions for user input
- **utils.py**: Utility functions for video processing and summarization
- **chroma_utils.py**: Functions for working with ChromaDB
- **groq_utils.py**: Functions for interacting with the Groq API

## Templates

- **base.html**: Base template with common structure
- **home.html**: Landing page
- **search.html**: Search form for YouTube videos
- **search_results.html**: Display search results
- **single_video_summary.html**: Form and result for single video summarization
- **summary.html**: Display generated summary
- **history.html**: User's search and summary history
- **login.html**: User login page
- **register.html**: User registration page
- **user_profile.html**: User profile and settings

## Static Files

- **styles.css**: Custom CSS styles
- **scripts.js**: Custom JavaScript functions

## Additional Files

- **requirements.txt**: Python package dependencies
- **.env**: Environment variables (not tracked in git)
- **.gitignore**: Specifies intentionally untracked files
- **README.md**: Project documentation and setup instructions

```bash
YoutubeSummarizer/
│
├── YoutubeSummarizer/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── summarizer/
│ ├── migrations/
│ │ └── init.py
│ ├── static/
│ │ ├── summarizer/
│ │ │ ├── css/
│ │ │ │ └── styles.css
│ │ │ └── js/
│ │ │ └── scripts.js
│ │ └── favicon.ico
│ ├── templates/
│ │ └── summarizer/
│ │   ├── base.html
│ │   ├── home.html
│ │   ├── search.html
│ │   ├── search_results.html
│ │   ├── single_video_summary.html
│ │   ├── summary.html
│ │   ├── history.html
│ │   ├── login.html
│ │   ├── register.html
│ │   └── user_profile.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── utils.py
│ ├── views.py
│ ├── chroma_utils.py
│ └── groq_utils.py
│
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```
