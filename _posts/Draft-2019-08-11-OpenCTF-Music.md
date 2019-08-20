---
layout: post
title:  "OpenCTF 2019 ~ Music"
author: Vivi
date:   2019-08-11 04:29:33 -0700
categories: CTF Stego Crypto DefCon27
tags: Stego OpenCTF Misc DefCon27
---

I was given to the opportunity to play with some of the smartest members of OpenToAll this year in OpenCTF @ DefCon 27. Although I only played for a short amount of time it was really fun and it re-inspired me to play in a lot more CTFs this year. This particular music question seemed very similar to the [QueerCon Music Puzzle]({{site.url}}/blog/ctf/stego/crypto/QC13-Soundcheck) and as such decided to tackle this down. 

/blog/ctf/crypto/Bach

I solved in 2016. lvedwas solved by me and can be found at at the  []()

	
**Contest Details**
---
[Music - 100](https://scoreboard.openctf.cat/challenges#Music) 
<figure>
   <img src="{{ site.github.url }}/images/openctf/Music.png" />
   <figcaption>musical_notes.jpg</figcaption>
</figure>''

```
Think you have solved the puzzle? Care to find out? 

Send your find to answer (at) queercon (dot) org; and we will let you know.   

Give up? Stay tuned for clues! They will be posted around in various places; such as on our Mobile App or Facebook page.  
```

Looks like we were given a song from Sound cloud. Given the clues, looks like there is some kind of hidden message in the song. Because the contest hinted: 

> Listen closely! Good luck!

I turned on the song for the next four hours while solving this puzzle to make sure it got stuck in my head.

Like any stego expert I downloaded the [full song]({{site.url}}/assets/queercon/Crypto [QueerCon13].mp3) from SoundCloud and looked at its metadata using exiftool which I saved [here]({{site.url}}/assets/queercon/Metadata.txt)


<figure>
<script type="text/javascript" src="https://asciinema.org/a/82493.js" id="asciicast-82493" async></script>
   <figcaption> Looking at the metadata</figcaption>
</figure>

As you can see, we got nothing from here. Referencing a few audio [writeups](https://github.com/ctfs/write-ups-2015/tree/master/polictf-2015/forensics/its-hungry), I thought I should try looking at its spectrogram. Using sox, the swiss army knife for audio manipulation, I made a spectrogram for the song. I did have some issues using sox with mp3 but I referenced [this super user post](http://superuser.com/questions/421153/how-to-add-a-mp3-handler-to-sox/421168) to convert it to a wav file or allow sox to run with mp3's. After which I ran spectrogram command:

<figure>
<script type="text/javascript" src="https://asciinema.org/a/c9ysl2rg2y2qixhgzd8btxlgh.js" id="asciicast-c9ysl2rg2y2qixhgzd8btxlgh" async></script>
   <figcaption> Making the spectrogram</figcaption>
</figure>

<figure>
   <img src="{{ site.github.url }}/images/queercon/spectrogram.png" />
   <figcaption>spectrogram.png</figcaption>
</figure>

As you can see there are few areas where the signal magnitude values (dBFS) are super high (where its yellow). Next step is to isolate each of these areas using Sox. The command I used was:

```
 sox <audio file> -n trim <time> <duration> spectrogram -o <ouput file>
```
> sox Crypto\ \[QueerCon13\].mp3 -n trim 1 1 spectrogram -o spectrogram-1-1.png

> sox Crypto\ \[QueerCon13\].mp3 -n trim 10 5 spectrogram -o spectrogram-10-5.png

> sox Crypto\ \[QueerCon13\].mp3 -n trim 65 5	 spectrogram -o spectrogram-65-5.png

> sox Crypto\ \[QueerCon13\].mp3 -n trim 110 5 spectrogram -o spectrogram-110-5.png

> sox Crypto\ \[QueerCon13\].mp3 -n trim 169 5 spectrogram -o spectrogram-169-5.png

The results were:

<div class="album">
   <figure>
      <img src="{{site.url}}/images/queercon/spectrogram-1-1.png" />
      <figcaption>spectrogram-1-1.png</figcaption>
   </figure>
   <figure>
      <img src="{{site.url}}/images/queercon/spectrogram-10-5.png" />
      <figcaption>spectrogram-10-5.png</figcaption>
   </figure>
    <figure>
      <img src="{{site.url}}/images/queercon/spectrogram-65-5.png" />
      <figcaption>spectrogram-65-5.png</figcaption>
   </figure>   
   <figure>
      <img src="{{site.url}}/images/queercon/spectrogram-110-5.png" />
      <figcaption>spectrogram-110-5.png</figcaption>
   </figure>   
   <figure>
      <img src="{{site.url}}/images/queercon/spectrogram-169-5.png" />
      <figcaption>spectrogram-169-5.png</figcaption>
   </figure>
</div>

This was amazingly hard to decipher so I pulled up [Sonic Visualizer](http://www.sonicvisualiser.org/) which lets me see a live spectrogram. It also has more room for users to zoom in and out in the spectrogram. Usage: Open Audio File ->  Shift + G (Spectrogram layer) -> Double Click Bottom Right Visible Range scale to adjust to according dBFS level. This were the results:

<div class="album">
   <figure>
      <img src="{{site.url}}/images/queercon/sonic1.png" />
      <figcaption>sonic1.png</figcaption>
   </figure>
   <figure>
      <img src="{{site.url}}/images/queercon/sonic2.png" />
      <figcaption>sonic2.png</figcaption>
   </figure>
    <figure>
      <img src="{{site.url}}/images/queercon/sonic3.png" />
      <figcaption>sonic3.png</figcaption>
   </figure>   
   <figure>
      <img src="{{site.url}}/images/queercon/sonic4.png" />
      <figcaption>sonic4.png</figcaption>
   </figure>   
   <figure>
      <img src="{{site.url}}/images/queercon/sonic5.png" />
      <figcaption>sonic5.png</figcaption>
   </figure>
</div>

My deciphering got me to think this text was: 

> **SALD LESUW TNDI UIKX NPTUC**

At this point in time I wasted a whole bunch time with ciphers at [http://rumkin.com/tools/cipher](http://rumkin.com/tools/cipher) such as caesars, vigenere...etc. Don't get me wrong I know how most of these work, why rebuild the wheel? I didn't really find anything here for a while. I tried other approaches such as looking at the metadata of the image that came along with the contest, but that didn't give me anything either. I even listened to the song like 50 more times to see if I missed anything. You can say I wasted like four hours here:

<figure>
   <img src="{{ site.github.url }}/images/queercon/musical_notes.jpg" />
   <figcaption>musical_notes.jpg</figcaption>
</figure>

Thinking I missed something back at [http://rumkin.com/tools/cipher](http://rumkin.com/tools/cipher), I tried the ciphers again and eventually got a hit with the playfair cipher. **NOTE: MAKE SURE YOU CHANGE TO DECRYPT INSTEAD OF ENCRYPT THE FIRST TIME TO MAKE SURE YOU DON'T WASTE FOUR HOURS TRYING OTHER CIPHERS**. As such I input the text we had *SALD LESUW TNDI UIKX NPTUC* and I got:

> **QCOA PARTY ROCK THIS HOUSE**

Something was obviously wrong with the first word so I looked back at the spectrograms and realized the "LD" in "SALD" was actually a "13" to make "SA13". This translates the final ciphertext to:

> **QC13 PARTY ROCK THIS HOUSE**

This was the 13th year for QueerCon so this made sense. I emailed contests@queercon.org which resulted in no response for a couple weeks. After which I saw on the QueerCon Facebook page that many people didn't get replies. I emailed one of the other QC ubers and was finally able to confirm I got the right answer along with a cool QC badge!

<figure>
   <img src="{{ site.github.url }}/images/queercon/QC13-Badge.jpg" />
   <figcaption>QueerCon Badge <br> *Photo from hackaday by Eric Evenchick*</figcaption>
</figure>

If you want a review of this year's badge feel free to head to [http://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/](http://hackaday.com/2016/08/10/what-we-learned-from-the-2016-queercon-badge/) Thanks again QueerCon for the awesome and fun challenge 