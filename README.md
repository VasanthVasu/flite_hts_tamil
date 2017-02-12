Flite HTS Tamil
===============
Simple text-to-speech tool for tamil drived from work done by SSN speech lab http://www.ssn.edu.in/Speech_Lab/Speech_home.html

Compilation
===========
	$ git clone git@github.com:men-tamil/flite_hts_tamil.git
	$ cd flite_hts_tamil
	$ make

Usage
=====
	$ cd flite_hts_tamil
	$ echo "வணக்கம்" | ./flite_tts_tamil -m asserts/naveen_tamil.htsvoice -o output.wav
	$ gst-play output.wav

Links
=====

* [htk](http://htk.eng.cam.ac.uk/) - implementation of hidden markov model
* [hts](http://hts.sp.nitech.ac.jp/) - speech synthesis on top of htk
* [flite](http://www.festvox.org/flite) - a fast speech synthesizer on top of htk
* [flitevox voice files](http://www.festvox.org/flite/packed/flite-2.0/voices) - voice files for flite.
* [comparison of open source text recognition toolkits](http://suendermann.com/su/pdf/oasis2014.pdf) - contains details about popular open source tts toolkits
* [kaldi](http://kaldi-asr.org/) - alternative to htk