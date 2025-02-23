# Public Space Intelligence System

## 🚀 Hackathon Showcase

### Overview
The **Public Space Intelligence System** is an innovative surveillance and monitoring solution designed to enhance safety and security in public spaces. It leverages **YOLO (You Only Look Once)** for real-time object and facial detection, along with **fire detection** to identify potential hazards. The system is powered by **Django and Python**, ensuring efficient processing and actionable insights.

## 🌟 Features

- **🧑‍🤝‍🧑 Face Detection**: Identifies and tracks human faces in public spaces.
- **🎯 Object Detection**: Detects and classifies objects in real-time.
- **🔥 Fire Detection**: Alerts in case of fire hazards, improving safety measures.
- **🔗 API Endpoints**: Provides a set of RESTful APIs for seamless integration.

## 🛠️ Tech Stack

- **Backend**: Django, Python
- **Machine Learning Models**: YOLO (for object and facial detection)
- **Database**: SQLite (default) / MySQL (optional)

## 🚀 Setup Instructions

### Prerequisites

Ensure you have the following installed before proceeding:

- Python 3.x
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/public-space-intelligence.git
   cd public-space-intelligence
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```sh
   python manage.py migrate
   ```

5. Run the server:

   ```sh
   python manage.py runserver
   ```

## 🎯 How It Works

- Start the server and access the web interface at:
  ```
  http://127.0.0.1:8000/
  ```
- Upload video streams or images for detection.
- Get real-time alerts for fire hazards.
- Use API endpoints to integrate with other applications.

## 💡 Why This Matters
- **Smart Surveillance**: Enhances monitoring in crowded areas.
- **Safety & Security**: Helps in early detection of potential hazards.
- **Automation**: Reduces manual effort in surveillance operations.

## 🤝 Contributing

We welcome contributions! If you have ideas for improvement or want to fix issues, feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

🎉 **Presented at [FOSS HUB] - [2025]!** 🎉

**Maintained by:** Team CGL - Coder's Got Latent

