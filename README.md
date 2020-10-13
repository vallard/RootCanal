# RootCanal
Small REST API to display file information from a portion of the users's file system. 

## How it works

The app will list metadata for a file and files in the directory. 

## App Behavior


Note, that symbolic links that may appear in the path are not followed.  

## Running the App

The app is a docker image.  The best way to run is to use docker compose: 

`docker-compose up -d`

This will run the application using your home directory as the root directory of the app.  To test the app is working you can run: 

`curl localhost` and you should see the contents of your `~/` directory. 




## Build Information

run `make`


## Testing

```
pip install pytest
cd <project root>
pytest
```

