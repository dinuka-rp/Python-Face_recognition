# Python-Face_recognition
This repository contains Python code that is capable of various face recognition functions.

This is my starting point in implementing Machine Learning algorithms for software solutions.

---

You can watch Traversy media's YouTube video that helped me get a kick start on facial recognition using machine learning [here](https://www.youtube.com/watch?v=QSTnwsZj2yc)

### Helpful GitHub repos to learn how to implement facial recognition using Python

[ageitgrey's face_recognition repo](https://github.com/ageitgey/face_recognition)<br/>
[Traversy media's face_recognition repo](https://github.com/bradtraversy/face_recognition_examples)

---

## How to install *dlib* face recognition library on Windows

I found myself wasting many hours trying to find a solution to get dlib to install properly using pip. Although I am aware that installing the Anaconda environment would ease the tedious process, I prefer not to install Anaconda as it takes up a large amount of unnecessary storage space. To make things easy for you, I've noted down a few steps that I followed to get the *dlib* library to get completely installed on Windows.

1. Open *pipenv* virtual environment in the terminal
2. Run "pip install cmake" in the terminal; to install cmake
3. Install Microsoft Build tools inorder to install C++ compiler
4. Run "pip install dlib" in the terminal
5. Run "pip install face_recognition" in the terminal<br/><br/>

You're good to go now!<br/>
You can even delete the Microsoft Build tools applications hereafter.<br/><br/>

*The dlib library only worked with Python when this method was followed.*<br/>


If you want to get the face_recognition library to work with C or C++, try to do so after installing MS Visual Studio.

Checkout ageitgrey's installation guide, to get this face_recognition library working on other platforms [here](https://github.com/ageitgey/face_recognition#installation)
