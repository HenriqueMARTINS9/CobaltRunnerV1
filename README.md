# Cobalt Runner Game
## Unity Editor
Download Unity Hub: https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup.exe 
Download version 2021.3.5f1 of the editor: https://unity.com/releases/editor/whats-new/2021.3.5 
Clone the git repo on your computer.
Open the project with Unity Hub and the correct version of the editor.

## Scenes
The two scenes are located in the Assets/Scenes folder. There are two scenes, one for the Menu and one for the Game.
Launch these scenes to observe them and make modifications.

## Firebase & WebGL
Follow the tutorial below:
https://medium.com/firebase-developers/firebase-with-unity-even-in-webgl-build-8891e6f9b33c 
Useful links for the tutorial:
Download Firebase CLI: https://firebase.tools/bin/win/instant/latest 
Add this package to Unity: https://github.com/rotolonico/FirebaseWebGL 

You can find the code created for the database connection in the Assets/Scripts/Firebase folder.
There is no connection with the database in the Unity editor.

## Build WebGL
To build the project, go to File -> Build Settings... in the editor. Make sure both scenes are present in "Scenes in Build," and Scenes/MainMenu is set to 0, and Scenes/RunnerGame is set to 1.
Select the WebGL platform if not already selected and click "Switch Platform."
Once done, you can choose to "Build" or "Build and Run."
Finally, if you have followed the tutorial from part 3 correctly, you should be able to play by connecting to the database.

## Important Folder
The important folders in this project are:
Assets/Runner
Contains audios, 3D objects with their materials and textures, characters with their animations, and prefabs.
Assets/Scripts
Contains scripts for collectible objects, environment, database, Menu, and character.


