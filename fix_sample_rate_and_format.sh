for x in sounds/*.wav; do
	mv "$x" "$x.tmp.wav"
	ffmpeg -i "$x.tmp.wav" -ac 2 -ar 48000 -sample_fmt s16 "$x"
	rm "$x.tmp.wav"
done
