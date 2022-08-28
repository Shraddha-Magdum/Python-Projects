# Import the dependencies
import pafy

# pip install youtube-dl
import moviepy.editor as mp

while True:

    # Menu
    print("-Menu-")
    print("Press 1 if you want to convert video to audio from your local video file ")
    print("Press 2 if you want to convert Youtube video to audio")
    print("Press 3 if you want to exit")

    # taking input from user
    c = input("Choice : ")
    print()

    # check if user entered correct input
    while not c.isnumeric():
        print()
        print("Enter choice again : ")
        c = input("Choice : ")
        print()

    # convert string value to int
    c = int(c)

    if c == 1:

        # taking input from user
        Video_File = input("Enter Video file name along with extension : ")
        Audio_File = input("Enter file name for converted audio (without extension) : ")

        # try-except block is used to handle the error
        try:
            # Insert Local Video File Path
            clip = mp.VideoFileClip(Video_File)

            # Insert Local Audio File Path
            Audio = clip.audio

            Audio.write_audiofile(Audio_File + ".mp3")

            # close the file
            clip.close()
            Audio.close()
            print()

        except:
            print()
            print("The video file could not be found! Please check that you entered the correct file name.")
            print()

    elif c == 2:
        # get url of youtube video from user
        url = input("Enter the url of Youtube video : ")

        # try-except block is used to handle the error
        try:
            # choose the video path
            Video = pafy.new(url)

            # extract audio from video
            audio = Video.getbestaudio()

            # download the video
            audio.download()
            print()

        except:
            print()
            print("Please check that you entered the correct url.")
            print()

    elif c == 3:
        print("Exiting the program!")
        break

    else:
        print("Wrong input !")
        print()

    # taking input from user
    choice = input("Do you want to perform this operation again if yes then enter y else n : ").upper()
    print()
    if choice == 'N':
        print("Exiting the program!")
        break
    elif choice != 'Y':
        print("Wrong input !")
        break
