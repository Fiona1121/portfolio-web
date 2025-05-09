# Fiona Wu's Clean One-Page Portfolio

This is a minimalist, single-page portfolio website built with Streamlit, designed to showcase my professional experience, projects, and skills in frontend engineering and creative technology.


## Features

- **Clean, Modern Design**: Simple, elegant layout with cards and subtle animations
- **Single-Page Format**: All information presented on one scrollable page
- **Responsive Layout**: Works well on both desktop and mobile devices
- **Minimal Navigation**: No sidebars or complex navigation to distract from content
- **Featured Projects**: Highlights of professional and personal work
- **Beyond Code**: Showcase of creative projects that go beyond programming

## Technologies Used

- **Streamlit**: Framework for building the web application
- **HTML/CSS**: Custom styling for a clean and modern look

## Requirements

- Python 3.7+
- Streamlit
- Pandas

## Installation & Setup

1. Clone this repository:
   ```
   git clone https://github.com/Fiona1121/streamlit-portfolio.git
   cd streamlit-portfolio
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Run

1. Make sure your virtual environment is activated.

2. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

3. The application will open in your default web browser at `http://localhost:8501`.

## Customization

To replace the placeholder image with your own:

1. Add your profile photo to the project directory
2. Update the image path in `app.py`:
   ```python
   # Change this line
   <img src="https://via.placeholder.com/300" class="profile-image">
   
   # To
   <img src="your_photo.jpg" class="profile-image">
   ```

## Deployment

This application can be deployed to Streamlit Cloud for free:

1. Push your code to a GitHub repository
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub account and select your repository
4. Deploy the application with a single click

## License

This project is licensed under the MIT License - see the LICENSE file for details.
