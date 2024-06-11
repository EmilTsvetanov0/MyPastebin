# MyPasteBin
A service similar to Pastebin but including automatic code language detection

## Requirements

You need:
- **Docker and docker-compose**
- **Language detection model**[Link to download](https://drive.google.com/file/d/1hz0tALaw8lajZHrfokGbViSSlHG6qpgN/view?usp=drive_link)

## Run the code
- Copy all the files in the repository to your local folder
- Copy downloaded previously model (file "model.pkl) to the "language-detection-model/model-folder/model.pkl" destination
- Go to the root folder where the "service" and "language-detection-model" folders are located and execute following command (!THE BUILDING PROCESS MAY TAKE MORE THAN 10 MINUTES!):
```
docker-compose build --no-cache
```
- Then to run the project execute following command:
```
docker-compose up
```
## To see the website go to the page "localhost:1333" or "127.0.0.1:1333" or "0.0.0.0:1333" in your browser
