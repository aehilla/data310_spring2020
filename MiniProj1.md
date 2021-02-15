# Responses for Mini Project 1: Social Distance Detector
### Feb 14

[input: video of people walking](https://www.videvo.net/video/people-walking-on-street/2181/)

[output from social distance detector (compressed)](output_of_walking_compressed.mp4)

1. Was your social distance detector effective at detecting potential violations? 

- The social distance detector script seemed like it was pretty effective for the video I used, which was just a stock video of lots of
people walking in a crowded city street. Most of the people were close together so most of the boxes in the output video were red, which is accurate.

2. Are you able to describe how the distance detector is applying its calculations of either being safe or noting a violation?

- From looking through the soc_dist_det.py script, it seems like it works by first defining a calibration function that checks whether
the distance between two people is large enough. It then defines a function to setup the layers, using the weights, cfg, and names files. 
I am not entirely sure what these files do in this function. I think the weights file must somehow tell the function what features of the input are most important.
The script then defines a processing function which I don't entirely understand but I think it's main purpose is to define a neural net that takes
the video as an input and which identifies people in the video and draws boxes around them, with the box colors depending on how far apart they are. 
Then the main body of the script uses these three functions to create a new output video, and it also times the processing speed per frame
and gives the total time taken to run the script. For the video I chose, the total time taken was 6.694753277301788 minutes. 

3. Do you think this approach would be effective for estimating new infections in real time? 

- I do not think this exact script would be that effective, because I input a 24 second video of people walking in a city street
and the script took almost 7 minutes to process it. This script would probably run faster on a more powerful computer but it still 
seems like it might be too slow to work in real time. I think this approach, generally speaking, is a good approach, but I think maybe the 
specifics of how the code is written would probably need to be made more efficient if this approach was going to be effective in real time.

4. How would you implement such an approach in response to the COVID-19 pandemic we are currently experiencing?

- If I had to implement an approach for real time, I would focus on stripping down the script so that it can run as quickly as possible
and thereby keep up with real time data constantly coming in. I think one way to do that would potentially be to find a way to reduce
the number of pixels in the input file to the minimum needed to identify people. This minimum would probably have to be found 
through some trial and error, but I think making the input frames of the videos into more simplified images would potentially make the 
script more efficient. 

5. What limitations or improvements might you include in order to improve your proposed design?

- I think a limitation of this approach would be that if there are other features in the input video that are vaguely human-shaped, then
by reducing the granularity of the input image as I suggested, it might increase the potential for the neural net to misidentify things as human and 
flag them for not social-distancing erroneously. This would make the script less useful, if the number of mis-identified social distancing
 violations was enough to slow down contact tracing for the correctly identified social distancing violations. 
