import download
import combine

if __name__ == '__main__':
	clips = download.download_clips()

	combine.stitch_clips(clips)