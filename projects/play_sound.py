import pygame

def play_mp3(file_path):
    # Initialize pygame mixer
    pygame.mixer.init()
    
    try:
        # Load the MP3 file
        pygame.mixer.music.load(file_path)
        
        # Play the music
        pygame.mixer.music.play()
        
        # Wait for music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(f"Error playing file: {e}")
    
    finally:
        # Clean up resources
        pygame.mixer.music.stop()
        pygame.mixer.quit()

if __name__ == "__main__":
    # Replace with the path to your MP3 file
    mp3_file_path = "D:\\Development\\software-python\\projects\\alarm.mp3"
    play_mp3(mp3_file_path)