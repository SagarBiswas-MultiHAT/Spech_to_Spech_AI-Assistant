# pip install pyaudio
# pip install SpeechRecognition
# pip install groq
# pip install pyttsx3

import speech_recognition as sr  # For capturing and recognizing speech
import webbrowser  # For opening URLs in a web browser
import pyttsx3  # For converting text to speech
import contentLinks  # Custom module (assumed for handling content links like music or videos)
from groq import Groq  # For interacting with the Groq API for AI responses
import time  # For managing time-related functions like delays

recognizer = sr.Recognizer()  # Initialize the speech recognizer for capturing and processing audio input
engine = pyttsx3.init()  # Initialize the text-to-speech engine for converting text to spoken words


def speak(txt, rate=150): # ...................................... XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (peak)_Function XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ......................................
    """
    Convert text to speech and speak it out loud.
    
    Parameters:
    txt (str): The text to be spoken.
    rate (int): The speed of the speech (words per minute).
    """
    engine.setProperty('rate', rate) # Set the speech rate (words per minute)
    engine.say(txt) # Queue(FIFO) the text to be spoken
    engine.runAndWait() # Process and play the speech

def listen_and_respond(duration=15, context=None): # ...................................... XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (Listen and Respond)_Function XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ...................................... 

    """
    Listen for audio commands and respond to them within a specified duration.
    
    Parameters:
    duration (int): The total time (in seconds) to keep listening and responding.
    context (dict): The conversation context to maintain continuity in responses.
    """

    start_time = time.time() # Record the start time
    r = sr.Recognizer()  # Initialize the speech recognizer

    while time.time() - start_time < duration:
        remaining_time = duration - (time.time() - start_time) # Calculate remaining time
        
        if remaining_time <= 0:
            break  # Exit the loop if the time is up

        try:
            with sr.Microphone() as source:
                print("\n--> Sagar listening...") # Notify that the bot is listening
                audio = r.listen(source, timeout=20, phrase_time_limit=5) # Listen for audio with a timeout and phrase time limit
                command = r.recognize_google(audio) # Convert audio to text
                print("\nCommand:", command) # Print the recognized command

                context = prossesCommand(command, context) # Process the command and update context
                start_time = time.time()  # Reset the start time to keep listening for another 15 seconds

        except sr.WaitTimeoutError:
            print("\nListening timed out while waiting for phrase to start.") # Handle timeout error

        except sr.RequestError as e:
            print(f"\nCould not request results from Google Speech Recognition service; {e}") # Handle request error

def aiProcess(command, context=None): # ...................................... XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (Ai Process)_Function XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ...................................... 

    """
    Generate a response to a command using the Groq API, incorporating conversation context.

    Parameters:
    command (str): The user's input command that needs to be processed.
    context (list of dict): The conversation history to provide context for generating a response.

    Returns:
    str: The generated response from the Groq API.
    """

    client = Groq(api_key="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") # Initialize the Groq API client with the provided API key

 # Create a list of messages to send to the Groq API
    messages = [
        {"role": "system", "content": "You are a virtual assistant named Sagar Biswas. You are skilled in general tasks like Alexa and Google Cloud. Generate texts that are appropriate for voice assistant. Must try to give short responses with perfect and understandable results."},
    ]

    # Include previous context if available to maintain conversation continuity
    if context:
        messages.extend(context)

    # Append the user's command to the messages list
    messages.append({"role": "user", "content": command})

     # Send the chat completion request to the Groq API and receive the response
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages
    )

    return completion.choices[0].message.content # Return the content of the generated response # why choices[0]? for the first message content? --> YES.

def prossesCommand(c, context=None): # ...................................... XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (Prosses Command)_Function XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ...................................... 

    """
    Process a user command and perform actions based on the command. 
    Update the conversation context with each interaction.

    Parameters:
    c (str): The command input from the user.
    context (list of dict): The conversation history to maintain continuity.

    Returns:
    list of dict: Updated conversation context including the latest interaction.
    """
    # Check if the command is to open a specific website
    if c.lower() == "open google": webbrowser.open("www.google.com")
    elif c.lower() == "open facebook": webbrowser.open("www.facebook.com")
    elif c.lower() == "open youtube": webbrowser.open("www.youtube.com")
    elif c.lower() == "open github": webbrowser.open("www.github.com")
    elif c.lower() == "open stack overflow": webbrowser.open("www.stackoverflow.com")
    elif c.lower() == "open linkedin": webbrowser.open("www.linkedin.com")
    elif c.lower().startswith("play"):
        try:
            words = c.lower().split(" ") # Extracting the song name from the command
            if len(words) > 1:
                song = words[1] # Get the song name
                link = contentLinks.Links.get(song, None) # Retrieve the link from the contentLinks module
                """
                The None here is used as the default value for the get method.
                Explanation:
                contentLinks.Links: This is likely a dictionary or a dictionary-like object.
                .get(song, None): The get method is used to retrieve the value associated with the key song.
                Why use None?
                Default Value: If the key song is not found in the dictionary Links, the get method returns None instead of raising a KeyError. This makes the code safer and avoids potential errors when accessing keys that might not exist.
                """
                if link:
                    webbrowser.open(link) # Open the song link in the browser
                else:
                    print("\n ..:: Song not found in the music library.") # Handle case where song is not found
            else:
                print("\n..:: No song specified.") # Handle case where no song is specified
        except Exception as e:
            print(f"Error: {e}") # Handle any exceptions that occur
    else:
        # Process the command using the AI process function and get a response
        output = aiProcess(c, context)
        print("\nAI Response:", output) # Print the AI response
        speak(output) # Convert the response to speech and speak it out

        # Update context with the latest interaction
        if context is None:
            context = [] # Initialize context if it is not provided

         # Append the user's command and the AI's response to the context
        context.append({"role": "user", "content": c})
        context.append({"role": "assistant", "content": output})

    return context  # Return the updated context


if __name__ == "__main__": # if __name__ == "__main__": checks if the script is being run directly, not imported. (Not a function, but a statement)...............................................................................................................................

    """
    Main entry point of the program. Continuously listen for commands, process them,
    and respond based on the context and user inputs.
    """
    context = None  # Initialize the conversation context to manage continuity

    while True:
        print("Recognizing...") # Indicate that the bot is starting to recognize speech
        try:
            r = sr.Recognizer() # Initialize the speech recognizer
            with sr.Microphone() as source:
                print("Listening...") # Indicate that the bot is listening for the activation word
                audio = r.listen(source, timeout=5, phrase_time_limit=2) # Listen for audio with a 5-second timeout and 2-second phrase limit

            word = r.recognize_google(audio)  # Convert the audio to text

            # Check if the recognized word is the activation word
            if word.lower() == "hey sagar":
                print("\nYes Boss! How Can I Assist You?") # Notify that the bot is now listening for commands
                speak("\nYes Boss! How Can I Assist You?")  # Respond to the activation word

                with sr.Microphone() as source:

                    print("\n--> Sagar listening...") # Notify that the bot is listening
                    audio = r.listen(source, timeout=20, phrase_time_limit=5)  # Capture audio for the command
                    command = r.recognize_google(audio) # Convert the command audio to text
                    print("\nCommand:", command) # Print the recognized command

                    # Process the command and update the context
                    context = prossesCommand(command, context) # Pass the context to maintain continuity

                    # Continue listening and responding based on the updated context
                    listen_and_respond(context=context) # Keep listening and responding for a specified duration

        except Exception as e:
            print(f"Timeout! {e} \n") # Print any errors that occur during execution
