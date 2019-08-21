---
layout: post
title:  "OpenCTF 2019 ~ Music"
author: Vivi
date:   2019-08-20 04:29:33 -0700
categories: CTF Stego Misc
tags: Stego OpenCTF Misc DefCon27
---

Finally got to play with some of the smartest members of OpenToAll this year in OpenCTF @ DefCon 27. Although I only played for a short amount of time it was really fun and it re-inspired me to play in a lot more CTFs this year. This particular [music question]((https://scoreboard.openctf.cat/challenges#Music) seemed very similar to the [QueerCon Music Puzzle]({{site.url}}/blog/ctf/stego/crypto/QC13-Soundcheck) I did in 2016 and figured it wouldn't be too hard to tackle. 


	
**Contest Details**
---

```
Music - 100
--------------
I think my computer is trying to send me a message.
```
Attached: [music.flac]({{site.url}}/assets/openctf2019/music.flac)

Seems like the author decided to hide a secret message within a [flac file]({{site.url}}/assets/openctf2019/music.flac). Listening to the file results in a single series of notes. Nothing fancy, like a beat, harmonics, melody, or anything of the sorts. Just to be sure I opened up a spectrogram to make sure no hidden messages were in the soundtrack.

<figure>
   <img src="{{ site.github.url }}/images/openctf2019/Spectogram-Music.png" />
   <figcaption>Spectrogram</figcaption>
</figure>

This spectrogram was created using [Sonic Visualizer](https://www.sonicvisualiser.org/download.html) which I discovered during the [QueerCon Puzzle]({{site.url}}/blog/ctf/stego/crypto/QC13-Soundcheck) I had mentioned before. Since than 2016, it has gone through a major rehaul and is very intuitive to use. I  can actually scroll, zoom, and export the Spectrogram using this tool. So much better than using:

```
 sox <audio file> -n trim <time> <duration> spectrogram -o <ouput file>
```

As you can see from the spectrogram no hidden high frequency tracks/sounds within the track. Next up was to look at the metadata:

<figure style="height: 75%">
<script id="asciicast-UbjMQ77DjMCfxAX28DpoHotO1" src="https://asciinema.org/a/UbjMQ77DjMCfxAX28DpoHotO1.js" async></script>
   <figcaption> Looking at the metadata</figcaption>
</figure>

Nothing here either except for maybe that it was processed by Sox, the command-line audio processing tool. I'm thinking if there are any unique transformations unique to Sox, it might be worth investigating. For now - I decided to put this on the backburner since this would require a lot of reading/guessing.

My next approach was to decipher the actual notes. There are two reasons for doing this:

1. The notes in this track are single notes. No overlapping notes nor magic frequencies. It seems a little too convenient that this music track was *considerably* easy to transcribe the notes.

<figure>
   <img src="{{ site.github.url }}/images/openctf2019/Spectogram-Music.png" />
   <figcaption>Spectrogram</figcaption>
</figure> 

2.) I figure if we can transcribe the notes, it might just be similar to a music challenge I solved called [Bach]({{site.url}}/blog/ctf/crypto/Bach) created by OpenToAll back in 2015 when the team was first created on on Reddit. In this particular music challenge, the notes eventually had a pattern that was easy to translate into letters of the alphabet.

|Normal|A|B|C|D|E|F|G|
|------|-----|----|-----|-----|-----|-----|-----|
|**Sharps**|H|I|J|K|L|M|N|
|**Naturals**|O|P|Q|R|S|T|U|
|**Flats**|V|W|X|Y|Z|

I Googled some OSX transcribing software and after trying a few here and there, the one that worked best was a tool called [AnthemScore](https://www.lunaverus.com) I opened the Music file on AnthemScore and let it process the Notes

<div class="album">
   <figure>
      <img src="{{ site.github.url }}/images/openctf2019/AnthemScore-Transcribe.png" />
       <figcaption>AnthemScore Transcribing Default Options</figcaption>
   </figure>
      <figure>
      <img src="{{ site.github.url }}/images/openctf2019/AnthemScore-Manual.png" />
       <figcaption>AnthemScore View</figcaption>
   </figure>
   <figure>
      <embed src="{{ site.github.url }}/assets/openctf2019/music.pdf" type="application/pdf">
      <figcaption>Transcription output</figcaption>
    </figure> 
</div>

Now that we had the notesm, the rest of the work was to identfy a common pattern. A lot of trial and error was followed. First thing I did was try to figure out the full range of the notes. Looking at the sheet music, there is roughly 16 unique notes. I mistakenly tried to translate the 16 notes into 26 letters. The math here being two octaves + two notes is roughly 12 notes (if you include the sharps/flats plus two notes). The result of this was something like 

After trying for a good 30 minutes of failing, I figure I should just turn the notes into numbers. Keep it simple and just turn the notes into numbers, something thats easier to see. The first note being a very low D is only the *second* lowest note in the whole sheet music. I marked this as two. The second note being the *highest* note in the whole sheet music. I marked this as 16 (since there were only actually 16 unique notes total)

With the help of the sheet music and the AnthemScore, The end result was something along the lines of 

```
2 16 9 12 1 9 1 9 4 6 12 15 5 7 6 13 1 1 1 4 7 7 7 13 7 2 7 8 3 15 8 5 8 9 8 5 1 1 5 12 13 12 5 11 5 13 11 16 3 15 13 15 3 16 13 14 5 12 3 10 9 13 5 14 11 11 5 12 9 11 11 9 11 11 5 12 9 16 5 16 13 10 5 16 3 14 13 15 3 12 8 9 13 16 3 13 11 10 15 6 1 3 1 1 11 5 4 15 1 5 4 3 2 16 1 1 1 1 1 1 1 1 1 1
```

With some a little big more time, some teamates on OpenToAll pointed out to me that there at 16 unique notes, which we can probably translate to *hex*. I took the current numbers I had and subtracted 1 from all to translate it to 0-15. Anything after 10 was changed into it's corresponding hexidecimal letter. The end result here was:

```
1F8B080835BE465C0003666C61672E747874004BCB494CAF2ECE2FCD4B298E4FCC4DACCACC4B8F4FC94F2DCE2B89CF2CA9E50200A43E04321F000000
```

I'm now thinking this might be an actual file and I need to write these bytes into one. I asked one of my teamates @uafio how to write raw text into a file and he gave me this piece of python code back

[WriteFile.py]({{site.github.url}}/assets/openctf2019/WriteFile.py)

```python
open('filename.raw', 'wb').write('1F8B080835BE465C0003666C61672E747874004BCB494CAF2ECE2FCD4B298E4FCC4DACCACC4B8F4FC94F2DCE2B89CF2CA9E50200A43E04321F000000'.decode('hex'))
```

I figure after running this and checking its file signatures we might have more insight onto how to get the flag

<figure>
<script id="asciicast-dTWaF0dQ5wEcJMoW6ILPVH5oI" src="https://asciinema.org/a/dTWaF0dQ5wEcJMoW6ILPVH5oI.js" async></script>
   <figcaption> Getting the final flag</figcaption>
</figure>

Viola! We have the flag


>**flag{sounds_amazing_doesnt_it}**

I submitted this flag on the scoreboard ahd got us another 100 points. At end of the day we OpenToAll was able to place second on the scoreboard. 

<figure>
   <img src="{{ site.github.url }}/images/openctf2019/FinalScore.png" />
   <figcaption>Final Score</figcaption>
</figure>

We had a lot of fun and want to thank everyone that helped organize OpenCTF this year at DefCon. Hope to see everyone next year