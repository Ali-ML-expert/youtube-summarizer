# 🚀 YouTube AI Summary App

## 📋 Description

The YouTube AI Summary App is a web application that allows users to summarize YouTube videos using AI. Users can search for videos, generate summaries, and view their summary history. The app is built with Django for the backend and React.js for the frontend, ensuring a responsive and user-friendly experience.

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** React.js, Bootstrap
- **Database:** SQLite
- **AI Integration:** Groq API
- **Data Processing:** ChromaDB, LangChain
- **Dependency Management:** Pipenv

## 📂 File Description

- **YoutubeSummarizer/**: Project root containing settings and configuration.
- **summarizer/**: Main application with core functionality.
- **templates/**: HTML templates for rendering views.
- **static/**: CSS, JavaScript, and other static files.
- **migrations/**: Database migration files.
- **manage.py**: Django's command-line utility for administrative tasks.
- **requirements.txt**: Python package dependencies.
- **.env**: Environment variables (not tracked in git).
- **.gitignore**: Specifies intentionally untracked files.

## 📝 Client Need

The client needs a web application that can summarize YouTube videos using AI. The app should allow users to search for videos, generate summaries, and view their summary history. The app should be responsive and user-friendly.

## 💡 Solution

The solution is a web application built with Django and React.js. The app integrates with the Groq API for AI summarization and uses ChromaDB and LangChain for data processing. The UI is designed with Bootstrap to ensure responsiveness and user-friendliness.

## 🔧 Options and Recommendations

- **Frontend Framework:** React.js is recommended for its component-based architecture and ease of integration with Django.
- **Styling:** Bootstrap is recommended for responsive design and pre-built components.
- **AI Integration:** Groq API is recommended for its powerful summarization capabilities.
- **Database:** SQLite is recommended for simplicity and ease of setup.

## 🚀 Install and Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/youtube-ai-summary-app.git
    cd youtube-ai-summary-app
    ```

2. **Set up the virtual environment:**

    ```bash
    pipenv install
    pipenv shell
    ```

3. **Set up the environment variables:**

    ```bash
    cp .env.example .env
    # Update .env with your configuration
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the tests:**

    ```bash
    python manage.py test_groq_connection
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the app in your browser:**
    ```http://127.0.0.1:8000/```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contribution

Contributions are welcome! Please fork the repository and submit a pull request.

## 🌟 Key Features

- **YouTube Scraping:** Scrape top results from YouTube for a given subject.
- **AI Summarization:** Use Groq API to summarize YouTube videos.
- **Responsive Design:** Ensure app is fully responsive across devices.
- **User Authentication:** Implement secure login and registration system.
- **Summary History:** View previously searched topics and summarized videos.
- **User Profile:** Manage user information, settings, and preferences.

## 📧 Contact

For any inquiries, please contact [amani.ali.upwork@gmail.com](mailto:your_email@example.com).

---

Thank you for using the YouTube AI Summary App! 🎉
