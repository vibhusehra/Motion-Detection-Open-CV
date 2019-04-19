<h2>Motion Detection using OpenCV</h2>
<p>Here we are using the openCV library to detect Motion in a video. </p>
<h3>How does this work?</h3>
<p>
We take 2 consecutive frames and try to detect any difference between the two frames.<br/>
If the difference in the mean of the 2 numpy arrays obtained is quite significant, we print 'Motion Detected'.
</p>
