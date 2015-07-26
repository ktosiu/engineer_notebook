FFMPEG
=======

Converting flv to mp4::

	ffmpeg -i input.flv -c:v libx264 -crf 19 output.mp4
	ffmpeg -i input.flv -c:v libx264 -crf 23 -c:a libfaac -q:a 100 output.mp4

Use `libx264 <https://trac.ffmpeg.org/wiki/Encode/H.264>`__ with -c:v (codec video) to 
encode. To improve the video quality, you can use a lower CRF value, e.g. anything down 
to 18. To get a smaller file, use a higher CRF, but note that this will degrade quality. 
Anything between 18 and 28 is reasonable with 23 being default.

To improve the audio quality, use a higher quality value (-q:a). For FAAC, 100 is default.