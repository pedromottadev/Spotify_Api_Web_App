# Spotify Data Explorer

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg" alt="Python" height="50" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" alt="Streamlit" height="50" />
  &nbsp;&nbsp;&nbsp;
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg" alt="Spotify" height="50" />
</p>

A web application built with **Python** and **Streamlit**, designed to interact with the **Spotify Web API** using the **Access Token** authentication method.  
This project demonstrates how to connect, query, and display Spotify data through a clear and responsive interface.



---

https://github.com/user-attachments/assets/07ffc733-a2a2-409f-ac48-79d973b159b4



## Overview

The application integrates with the [Spotify Web API](https://developer.spotify.com/documentation/web-api) to retrieve and display information about artists, top musics and ranking position.  
It serves as a  example of Spotify API integration and data visualization using Python and Streamlit.

---

## Key Features

- Authentication using Spotify’s **Access Token** method  
- Retrieval of track, album, and artist metadata  
- Real-time data display with Streamlit  
- Python code structure  

---

## Technologies

- **Python 3.10+**  
- **Streamlit** – front-end framework for data apps  
- **Requests** – HTTP client for API communication  
- **Spotify Web API** – data source  

---

## Authentication

This application uses Spotify’s **Access Token** method for authentication.  
You can generate tokens directly from the [Spotify Developer Console](https://developer.spotify.com/documentation/web-api).

> - Note: Access tokens expire periodically. You must refresh or request a new token to maintain access.
> ###  !! create the *.env* to protect your keys !!

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/spotify-api-streamlit.git
   cd spotify-api-streamlit
