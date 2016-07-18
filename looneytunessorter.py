#!/usr/bin/env python
import os
from utilities.media_collector import MediaFileCollector

directory_to_rename = '/Volumes/Xanadu-Plex/Looney Tunes Golden Collection'

class LooneyTunesRenamer(object):
	"""docstring for LooneyTunesSorter"""
	def __init__(self):
		super(LooneyTunesRenamer, self).__init__()
	def rename(self, raw_files):
		for video_file in raw_files:
			# print video_file
			directory = os.path.dirname(video_file)
			original_file_name = os.path.basename(video_file)
			renamed_file_name = original_file_name[5:]
			renamed_file_path = os.path.join(directory, renamed_file_name)
			print renamed_file_path
			os.rename(video_file, renamed_file_path)


def main():
	print 'Renaming Looney Tunes'
	collector = MediaFileCollector(directory_to_rename)
	renamer = LooneyTunesRenamer()
	renamer.rename(collector.all_files())

if __name__ == "__main__":
	main()
