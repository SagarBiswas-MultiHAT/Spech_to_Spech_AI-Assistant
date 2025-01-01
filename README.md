### README.md

# Voice-Controlled Virtual Assistant: "Hey Sagar"

![Voice-Controlled Virtual Assistant](https://scontent.fdac138-1.fna.fbcdn.net/v/t39.30808-6/472300904_122132627642552158_7597006921599684126_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=abH9yBDiVM4Q7kNvgFbmPZP&_nc_zt=23&_nc_ht=scontent.fdac138-1.fna&_nc_gid=AQesYnXkH9k84QIr0_DsnbB&oh=00_AYCzzBzw8plN_IBiZlHmauMpzocBEBwkhLWdRW0X1khHjA&oe=677ADC39)

This repository contains a Python-based voice-controlled virtual assistant designed to handle commands like opening websites, playing music, and generating AI-based responses. Powered by Google’s Speech Recognition, Groq API, and pyttsx3, it offers a seamless and interactive user experience.  

---

## Features  
- **Voice Activation:** Trigger the assistant with the keyword `"Hey Sagar"`.  
- **Speech-to-Text:** Uses Google Speech Recognition to capture and process audio commands.  
- **AI-Powered Responses:** Processes commands and generates context-aware responses using the Groq API.  
- **Text-to-Speech:** Responds audibly using pyttsx3 for a natural voice experience.  
- **Web Automation:** Opens popular websites (e.g., Google, YouTube) and plays music links.  
- **Context Awareness:** Maintains conversation context for better interactions.  

---

## Prerequisites  

Ensure the following Python libraries are installed:  
```bash  
pip install pyaudio  
pip install SpeechRecognition  
pip install pyttsx3  
pip install groq  
```  

---

## Setup and Configuration  

1. Clone this repository:  
   ```bash  
   git clone <repository-url>  
   cd <repository-folder>  
   ```  

2. Install the required libraries (see prerequisites).  

3. Replace the `api_key` in the `aiProcess()` function with your Groq API key.  

4. Run the script:  
   ```bash  
   python <script-name>.py  
   ```  

---

## How to Use  

1. **Start Listening:** Run the script, and the assistant waits for the activation phrase `"Hey Sagar"`.  

2. **Give Commands:** Speak commands like:  
   - "Open Google"  
   - "Play [song_name]"  
   - General queries for AI responses (e.g., "What's the weather?").  

3. **AI Response:** The assistant will process your command and provide a response or action audibly and visually.  

---

## Supported Commands  

| Command Example       | Action                        |  
|------------------------|-------------------------------|  
| "Open Google"          | Opens `www.google.com` in a browser. |  
| "Open YouTube"         | Opens `www.youtube.com`.     |  
| "Play [song_name]"     | Searches and plays a song.   |  
| Custom questions       | AI-generated response based on input. |  

---

## Customization  

- **Add More Commands:** Extend the `prossesCommand()` function to handle new commands.  
- **Change Voice Settings:** Modify `speak()` to adjust speed, pitch, or voice settings.  

---

## Notes  

- **Microphone Access:** Ensure your microphone is configured and accessible.  
- **API Key:** A valid Groq API key is required for AI responses.  

---

## License  

This project is open-source and available under the [MIT License](LICENSE).  

---

## Contributing  

Contributions are welcome! Feel free to fork the repository and submit pull requests for enhancements or bug fixes.  

---

Enjoy using your very own voice assistant! 😊
